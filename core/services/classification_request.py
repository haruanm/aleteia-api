""" This modules contains the services to handle the core.models.ClassificationRequest """
from aleteia_classificator.services.evaluation import FakeNewsTextEvaluator
from core.models import ClassificationRequest


class ClassificationRequestService:
    """ This class have the business rules for the core.models.ClassificationRequest """

    def __init__(self, classification_request=None):
        if classification_request is not None:
            self.classification_request = classification_request

    def create_request(self, text, url, ipv4=None, ipv6=None):
        """
        Create a classification request instance with the info
        :param text: text to be classified
        :param url: url of the website
        :param ipv4: ipv4 of the requester
        :param ipv6: ipv6 of the requester if existis
        """
        self.classification_request = ClassificationRequest(**{
            'text': text,
            'url': url,
            'ipv4': ipv4,
            'ipv6': ipv6
        })
        self._evaluate_request()
        return self.classification_request

    def _evaluate_request(self):
        """ Evaluate the request using Aleteia's classifier """
        evaluator = FakeNewsTextEvaluator([self.classification_request.text])
        self.classification_request.response = {'response': evaluator.predict()[0]}
        self.classification_request.save()
