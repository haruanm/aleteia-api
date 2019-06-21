from django.core.management.base import BaseCommand
from aleteia_classificator.services.training import FakeNewsTextTrainer
from core.services.news import NewsService


class Command(BaseCommand):
    """ Command to train Aleteia's model"""
    help = 'Train Aleteia'

    def handle(self, *args, **options):
        """ Get all labeled news and train the model

        :param args:
        :param options:
        """
        news_service = NewsService()
        labeled_news = news_service.get_labeled_news()
        trainer = FakeNewsTextTrainer(labeled_news[0], labeled_news[1])
        trainer.train()
