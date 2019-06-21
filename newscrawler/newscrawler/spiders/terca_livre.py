from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TercaLivreSpider(CrawlSpider):
    """ Spyder to crawling news """
    name = 'terca_livre'
    allowed_domains = ['tercalivre.com.br']
    start_urls = ['https://www.tercalivre.com.br/']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        """
        Parses the html content for each crawled page
        :param response: void
        """
        new = ''
        for new_body in response.css('.entry-content p'):
            new += new_body.get().strip()

        if len(new) > 0:
            yield {
                'title': response.css('h1.entry-title ::text').get().strip(),
                'date': response.xpath("//meta[@property='article:published_time']/@content")[0].extract(),
                'text': new,
                'url': response.url
            }
