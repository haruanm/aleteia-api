from django.core.management.base import BaseCommand
from aleteia_classificator.services.training import FakeNewsTextTrainer
from core.services.news import NewsService
import nltk

class Command(BaseCommand):
    """ Command to train Aleteia's model"""
    help = 'Train Aleteia'

    def handle(self, *args, **options):
        """ Download nltk content

        :param args: list of params (will be ignored)
        :param options: dict of options (will be ignored)
        """
        nltk.download('stopwords')
        nltk.download('rslp')
        nltk.download('punkt')

