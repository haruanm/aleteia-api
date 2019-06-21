import os

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Crawl news'

    def handle(self, *args, **options):
        """
        Run the webcrawler for each desired site
        :param args:
        :param options:
        """
        os.chdir('newscrawler')
        for spider in settings.SPIDERS:
            os.system('scrapy crawl {}'.format(spider))
