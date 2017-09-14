import copy

from scrapy import Spider
from scrapy.http.request import Request
from scrapy.http.response import Response

from iarc.items import IarcItem


class TopographySpider(Spider):
    name = "topography"
    start_urls = ["http://codes.iarc.fr/topography"]

    def parse(self, response: Response):
        current_code1 = None
        for code in response.css("#main > #content > #content-inner > span.text"):
            if len(code.css('b')) != 0:
                current_code1 = code.css('b::text').extract_first().strip()
                continue
            else:
                current_item = IarcItem()
                current_item['code1'] = current_code1
                current_item['code2'] = code.css('::text').extract_first().strip()
                current_item['code2_name'] = code.css('a::text').extract_first().strip()
                yield Request(response.urljoin(code.css('a').xpath('@href').extract_first()),
                              self.parse_code2, meta={'item': current_item})

    def parse_code2(self, response):
        for code in response.css("a::text").re(r"\d+/\d+\s.*"):
            item = copy.copy(response.meta['item'])
            code3, code3_name = code.split(" ", 1)
            item['code3'] = code3
            item['code3_name'] = code3_name
            yield item
