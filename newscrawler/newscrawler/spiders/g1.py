import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','???.settings')

import django
django.setup()
from core.models import News
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class G1Spider(CrawlSpider):
    """ Spyder to crawling news from g1 """
    name = 'g1'
    allowed_domains = ['g1.globo.com']
    start_urls = ['https://g1.globo.com/']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        """
        Parses the html content for each crawled page
        :param response: void
        """
        new = ''
        for new_body in response.css('.content-text__container'):
            new += new_body.get().strip()

        if len(new) > 0:
            News.objects.create(
                url=response.url,
                date=response.xpath("//meta[@itemprop='datePublished']/@content")[0].extract(),
                title=response.css('h1.content-head__title ::text').get().strip(),
                text=new
            )
