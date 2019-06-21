""" This module contains the service to train the data """
from time import time
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

from joblib import dump
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import KFold

import nltk
from nltk.stem import RSLPStemmer


class AleteiaTokenizer:
    def __call__(self, text):
        """ Tokenize the text

        :param text: text to be tokenized
        :return: a tokenized text
        """
        tokens = self._tokenize(text)
        stemmed_tokens = self._stem(tokens)
        return self._remove_stop_words(stemmed_tokens)

    @staticmethod
    def _remove_stop_words(text):
        """ Remove stop words of the text

        :param text: list of words to be checked
        :return: list of words without stop words
        """
        stopwords = nltk.corpus.stopwords.words('portuguese')
        phrase = []
        for word in text:
            if word not in stopwords:
                phrase.append(word)
        return phrase

    @staticmethod
    def _stem(text):
        """ Convert words to it's stem

        :param text: list of words
        :return: list of stemmed words
        """
        stemmer = RSLPStemmer()
        phrase = []
        for word in text:
            phrase.append(stemmer.stem(word.lower()))
        return phrase

    @staticmethod
    def _tokenize(text):
        """ Make words lower case and split them

        :param text: text to be tokenized
        :return: list of words
        """
        text = text.lower()
        text = nltk.word_tokenize(text)
        return text


class FakeNewsTextTrainer:
    def __init__(self, news, labels):
        """ Init the instance and set items to be tested

        :param news: list of texts to be used for training
        :param labels: list of categories of the texts
        """
        self.start = time()
        self.news = news
        self.labels = labels
        self.vectorizer = CountVectorizer(ngram_range=(1, 1), tokenizer=AleteiaTokenizer())
        self.dimension_reducer = SelectKBest(chi2, k=10350)

    def _get_processed_text(self):
        """ Process the text to reduce noise and make it good for train

        :return: Tokenized text good to use
        """
        vectorized_news = self.vectorizer.fit_transform(self.news)
        print('Vectorized news: {:.2f}s'.format(time()-self.start))

        reduced_vectorized_news = self.dimension_reducer.fit_transform(vectorized_news, self.labels)

        print('Reduced Vectorized news: {:.2f}s'.format(time()-self.start))

        return reduced_vectorized_news

    def _save_model(self, model):
        """ Save the trained model to files

        :param model: model to be saved
        """
        dump(self.vectorizer, 'resources/vectorizer.joblib')
        dump(model, 'resources/token_SVM.joblib')
        dump(self.dimension_reducer, 'resources/dimension_reducer.joblib')

    @staticmethod
    def _train(x_train, y_train):
        """ Trains a SVM and returns it

        :param x_train: features to be used in the training
        :param y_train: labels to be used in the training
        :return: trained SVM
        """
        model = SVC(gamma='auto')
        model.fit(x_train, y_train)
        return model

    def train(self):
        """ Train Aleteia's model and save it to allow future predictions """
        vectorized_news = self._get_processed_text()

        x_train_validation, x_test, y_train_validation, y_test = train_test_split(vectorized_news, self.labels,
                                                                                  random_state=777, test_size=.3)
        y_train_validation = np.array(y_train_validation)

        kfold = KFold(n_splits=5, random_state=777, shuffle=True)
        best_model = None
        accuracy = 0
        for train_index, val_index in kfold.split(x_train_validation):

            model = self._train(x_train_validation[train_index],
                                y_train_validation[train_index])
           
            y_train_validation_predicted = model.predict(x_train_validation[val_index])
            new_accuracy = accuracy_score(y_train_validation[val_index], y_train_validation_predicted)

            if new_accuracy > accuracy:
                accuracy = new_accuracy
                best_model = model

        y_test_predicted = best_model.predict(x_test)

        print(accuracy_score(y_test, y_test_predicted))
        
        print('Trained: {:.2f}s'.format(time()-self.start))

        print(classification_report(y_test, model.predict(x_test), target_names=['True', 'Fake']))
        print(confusion_matrix(y_test, model.predict(x_test)))

        self._save_model(model)

        print('Model Saved: {:.2f}s'.format(time()-self.start))
