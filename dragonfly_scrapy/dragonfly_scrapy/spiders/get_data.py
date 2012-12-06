# -*- coding: utf-8 -*-
import sys
from urllib import urlencode
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request, FormRequest

from dragonfly_scrapy.items import CountryItem, RegimeItem, AduanaItem

class GetDataAduanet(BaseSpider):
    name = "abracadabra"
    domain = "http://www.aduanet.gob.pe"
    start_urls = [
        "http://www.aduanet.gob.pe/cl-ad-itconsultadwh/ieITS01Alias?accion=consultar&CG_consulta=4",
    ]

    urls = {
        'initial': 'http://www.aduanet.gob.pe/cl-ad-itconsultadwh/ieITS01Alias',
        'dua_list': "http://www.aduanet.gob.pe/cl-ad-itconsultadwh/ieITS01Alias?",
    }

    def __init__(self, name=None, **kwargs):
        self.CG_consulta = '4' #Parametro de la url inicial que nos envio Toni :P
        self.CG_regimen = '10' #Importación

        # Extracción de parametros: Año y Mes
        try:
            self.CG_anio = kwargs['year']
            self.CG_mes = kwargs['month']
        except KeyError:
            print "***** Using for example: scrapy crawl %s -a year=2012 -a month=04" % self.name
            sys.exit(0)

        super(GetDataAduanet, self).__init__(name=name, **kwargs)


    def parse(self, response):
        """ Consulta de importaciones.
        """
        #countries = CountryItem.django_model.objects.all()
        #aduanas = AduanaItem.django_model.objects.all()
        hxs = HtmlXPathSelector(response)
        cod_anio = hxs.select('//select[@name="CG_Ano"]/option[text()="%s"]' % self.CG_anio
                ).select('@value').extract()[0]

        countries = CountryItem.django_model.objects.filter(code='CN')
        aduanas = AduanaItem.django_model.objects.filter(code='019')

        requests = []

        for country in countries:
            for aduana in aduanas:
                formdata = {
                    'CG_Aduana': aduana.code,
                    'CG_Ano': cod_anio,
                    'CG_Mes': self.CG_mes,
                    'CG_Pais': country.code,
                    'CG_consulta': self.CG_consulta,
                    'CG_regimen': self.CG_regimen,
                    'accion': 'buscarListadoImpoExpo'
                }

                requests.append(
                    FormRequest(url=self.urls['initial'],
                        formdata=formdata,
                        callback=self.agent_list)
                    )
        return requests

    def agent_list(self, response):
        # Creación de agentes y validación si existen.
        hxs = HtmlXPathSelector(response)
        js_params = hxs.select('//tr[@class="bg"]/td[1]/a/@href').extract()
        
        requests = []

        for js_param in js_params:
            param_list = js_param[js_param.find('("')+2: js_param.find('")')].split('","')
            param = {
                'CG_consulta': self.CG_consulta,
                'CG_regimen': self.CG_regimen,
                'CG_aduana': param_list[1],
                'CG_agente': param_list[2],
                'CG_mes': param_list[3],
                'CG_anio': param_list[4],
                'CG_Pais': param_list[5],
                'accion':  'buscarListadoDuas'
            }

            url = self.urls['dua_list'] + urlencode(param)
            requests.append(Request(url=url, callback=self.dua_list))
        return requests
        

    def dua_list(self, response):
        # Crear la DUA y validar que la dua sea única
        hxs = HtmlXPathSelector(response)
        duas = hxs.select('//tr[@class="bg"]/td[3]/a/@href').extract()
        requests = []
        for dua in duas:
            requests.append(Request(url=dua, callback=self.dua_detail))
        return requests

    def dua_detail(self, response):
        hxs = HtmlXPathSelector(response)

        xpath_dua_report = "/html/body/center/a[5]/@href"
        xpath_dua_formatb = "/html/body/center/a[4]/@href"
        xpath_dua_container_list = "/html/body/center/b/a/@href"

        url_dua_report = hxs.select(xpath_dua_report).extract()[0]
        url_dua_formatb = hxs.select(xpath_dua_formatb).extract()[0]
        url_dua_container_list = hxs.select(xpath_dua_container_list).extract()[0]

        requests = [
            Request(url=self.domain + url_dua_report, callback=self.dua_report),
            Request(url=self.domain + url_dua_formatb, callback=self.dua_formatb),
            Request(url=self.domain + url_dua_container_list, callback=self.dua_container_list),
        ]
        return requests

    def dua_report(self, response):
        # Seleccionar la DUA y actualizar sus datos. Aqui se crean las demas entidades.
        hxs = HtmlXPathSelector(response)
        print hxs.select("/html/body/table[1]/tr[2]/td[2]/font/text()").extract()[0]

    def dua_container_list(self, response):
        # Extraer listado de contenedores, crear contenedores y asociarlos a la DUA
        pass

    def dua_formatb(self, response):
        xpath_declaracion_valor = "/html/body/table/tr[2]/td/font/a/@href"
        hxs = HtmlXPathSelector(response)
        url_declaracion_valor = hxs.select(xpath_declaracion_valor).extract()[0]
        return Request(url=self.domain + url_declaracion_valor, callback=self.dua_formatob_declaracion)

    def dua_formatob_declaracion(self, response):
        # Extraer declarante, crear declarante y asociarlo a la dua
        pass


        