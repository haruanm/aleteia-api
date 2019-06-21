from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DCMSpider(CrawlSpider):
    """ Spyder to crawling news from Diario do Centro do Mundo"""
    name = 'dcm'
    allowed_domains = ['diariodocentrodomundo.com.br']
    start_urls = ['https://www.diariodocentrodomundo.com.br/']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        """
        Parses the html content for each crawled page
        :param response: void
        """
        new = ''
        for new_body in response.css('.td-post-content p'):
            new += new_body.get().strip()

        if len(new) > 0:
            yield {
                'title': response.css('h1.entry-title ::text').get().strip(),
                'date': response.xpath("//meta[@itemprop='datePublished']/@content")[0].extract(),
                'text': new,
                'url': response.url
            }
