from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class FolhaSpider(CrawlSpider):
    """ Spyder to crawling news from Folha de São Paulo"""
    name = 'folha'
    allowed_domains = ['folha.uol.com.br']
    start_urls = ['https://www.folha.uol.com.br/']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        """
        Parses the html content for each crawled page
        :param response: void
        """
        new = ''
        for new_body in response.css('.c-news__body p'):
            new += new_body.get().strip()

        if len(new) > 0:
            yield {
                'title': response.css('h1.c-content-head__title ::text').get().strip(),
                'date': response.xpath("//meta[@property='article:published_time']/@content")[0].extract(),
                'text': new,
                'url': response.url
            }
