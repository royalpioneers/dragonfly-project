# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from dragonfly_scrapy.items import CountryItem, RegimeItem, AduanaItem

class InitialDataAduanet(BaseSpider):
    name = "initial_data"
    allowed_domains = ["http://www.aduanet.gob.pe"]
    start_urls = [
        "http://www.aduanet.gob.pe/cl-ad-itconsultadwh/ieITS01Alias?accion=consultar&CG_consulta=4",
    ]

    def __init__(self, name=None, **kwargs):
        self.country_selector = '//select[@id="CG_Pais"]/option'
        self.aduana_selector = '//select[@id="CG_Aduana"]/option'
        self.regime_selector = '//select[@name="CG_regimen"]/option'
        super(InitialDataAduanet, self).__init__(name=name, **kwargs)


    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        # Creación de paises de origen
        for country_hxs in hxs.select(self.country_selector):
            country = CountryItem()
            country['code'] = country_hxs.select('@value').extract()[0]
            country['name'] = country_hxs.select('text()').extract()[0]
            country.save()

        # Creación de aduanas
        for aduana_hxs in hxs.select(self.aduana_selector):
            aduana = AduanaItem()
            aduana['code'] = aduana_hxs.select('@value').extract()[0]
            aduana['name'] = aduana_hxs.select('text()').extract()[0][6:]           
            aduana.save()

        # Creación de regimen
        for regime_hxs in hxs.select(self.regime_selector):
            regime = RegimeItem()
            regime['code'] = regime_hxs.select('@value').extract()[0]
            regime['name'] = regime_hxs.select('text()').extract()[0]
            regime.save()