
class ProxyMiddleware(object):

    def process_request(self, request, spider):
        """
        Add a proxy to the request
        :param request: scrapy request
        :param spider: spider that is doing the request
        """
        request.meta['proxy'] = "http://proxy:16379"

