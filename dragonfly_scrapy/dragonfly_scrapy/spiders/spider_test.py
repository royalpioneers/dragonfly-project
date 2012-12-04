from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import random

from dragonfly_scrapy.items import ProductItem

class TestSpider(BaseSpider):
    name = "test"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ul/li')
        items = []
        for site in sites:
            item = ProductItem()
            item['hs'] = random.randrange(4,10)
            items.append(item)
        return items
