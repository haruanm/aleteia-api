from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class OGloboSpider(CrawlSpider):
    """ Spyder to crawling news from oglobo portal"""
    name = 'oglobo'
    allowed_domains = ['oglobo.globo.com']
    start_urls = ['https://oglobo.globo.com/']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        """
        Parses the html content for each crawled page
        :param response: void
        """
        new = ''
        for new_body in response.css('.protected-content p'):
            new += new_body.get().strip()

        if len(new) > 0:
            yield {
                'title': response.css('h1.article__title ::text').get().strip(),
                'date': response.xpath("//meta[@property='article:published_time']/@content")[0].extract(),
                'text': new,
                'url': response.url
            }
