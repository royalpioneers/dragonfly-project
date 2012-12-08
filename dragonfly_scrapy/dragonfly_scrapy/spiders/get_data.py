# -*- coding: utf-8 -*-
import sys
from datetime import datetime, date
from decimal import Decimal
from urllib import urlencode
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request, FormRequest

from dragonfly_scrapy.items import CountryItem, RegimeItem, AduanaItem, \
    AgentItem, ContainerItem, SupplierItem, PortItem, ImporterItem, \
    DeclaranteItem, StatusItem, TransportItem, DuaItem, Hs, Item, HtsItem, \
    ProductItem, DetalleDua

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
        self.regime_object = RegimeItem.django_model.objects.get(code=self.CG_regimen)

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
                        callback=self.agent_list,
                        meta={'aduana': aduana})
                    )
        return requests

    def agent_list(self, response):
        hxs = HtmlXPathSelector(response)
        js_params = hxs.select('//tr[@class="bg"]/td[1]/a/@href').extract()
        requests = []

        for js_param in js_params:
            param_list = js_param[js_param.find('("')+2:js_param.find('")')].split('","')
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
            # Creación del agente
            agent_name = hxs.select(
                """//tr[@class="bg" and td[1]/a[@href='%s']]/td[2]/text()""" % js_param
                ).extract()[0]
            agent, created = AgentItem.django_model.objects.get_or_create(code=param['CG_agente'],
                  defaults={'name': agent_name})

            # Creación de los requests
            url = self.urls['dua_list'] + urlencode(param)
            requests.append(Request(url=url, callback=self.dua_list, 
                meta={'aduana': response.meta['aduana'], 'agent': agent}))

        return requests
        

    def dua_list(self, response):
        # Crear la DUA y validar que la dua sea única
        hxs = HtmlXPathSelector(response)
        duas = hxs.select('//tr[@class="bg"]')

        requests = []
        for dua in duas:
            # Creación de la DUA
            code = "%(aduana)s-%(anio)s-%(regimen)s-%(ndeclaracion)s-00"
            values_code = {
                'aduana': dua.select('td[1]/text()').extract()[0],
                'anio': dua.select('td[2]/text()').extract()[0],
                'regimen': self.CG_regimen,
                'ndeclaracion': dua.select('td[3]/a/text()').extract()[0],
            }
            dua_object, created = DuaItem.django_model.objects.get_or_create(
                code=code%values_code, defaults={})
            if created:
                dua_object.regime = self.regime_object
                dua_object.aduana = response.meta['aduana']
                dua_object.agent = response.meta['agent']
                dua_object.save()

            # Creación de los requests
            url_dua = dua.select('td[3]/a/@href').extract()[0]
            meta_data = {'dua': dua_object}
            requests.append(
                Request(url=url_dua, callback=self.dua_detail, meta=meta_data)
                )
        return requests

    def dua_detail(self, response):
        hxs = HtmlXPathSelector(response)

        xpath_dua_report = '//a[b/font/text()="Reporte DUA"]/@href'
        xpath_dua_formatb = '//a[b/font/text()="Formato B"]/@href'
        xpath_dua_container_list = '//a[font/b/text()="Relacion de Contenedores"]/@href'

        try:
            url_dua_report = hxs.select(xpath_dua_report).extract()[0]
            url_dua_formatb = hxs.select(xpath_dua_formatb).extract()[0]
            url_dua_container_list = hxs.select(xpath_dua_container_list).extract()[0]
        except IndexError:
            print response.meta['dua'].code

        requests = [
            Request(url=self.domain + url_dua_report, 
                callback=self.dua_report, meta={'dua': response.meta['dua']}),
            Request(url=self.domain + url_dua_formatb, 
                callback=self.dua_formatb, meta={'dua': response.meta['dua']}),
            Request(url=self.domain + url_dua_container_list, 
                callback=self.dua_container_list, meta={'dua': response.meta['dua']}),
        ]
        return requests

    def dua_report(self, response):
        # Seleccionar la DUA y actualizar sus datos. Aqui se crean las demas entidades.
        hxs = HtmlXPathSelector(response)
        dua = response.meta['dua']

        # Creamos el Importador
        importer_ruc = hxs.select('/html/body/table[1]/tr[6]/td[2]/font/text()'
            ).extract()[0].split('-').pop()
        importer_name = hxs.select('/html/body/table[1]/tr[6]/td[3]/font/text()').extract()[0]
        importer_address = hxs.select('/html/body/table[1]/tr[6]/td[5]/font/text()').extract()[0]
        importer, created = ImporterItem.django_model.objects.get_or_create(code=importer_ruc,
            defaults={'name': importer_name, 'address': importer_address})
        dua.importer = importer

        # Agregamos fecha de llegada a la dua
        dua.fecha_llegada = datetime.strptime(
            hxs.select('/html/body/table[1]/tr[11]/td[6]/font/text()').extract()[0],
            "%d/%m/%Y"
            ).date()

        # Creamos y asociamos el status

        # Creamos el puerto y lo asociamos
        port_data = hxs.select('/html/body/table[2]/tr[9]/td[2]/font/text()').extract()[0]
        port, created = PortItem.django_model.objects.get_or_create(
            code=port_data.split('-')[0], defaults={'name':port_data.split('-')[1]})
        dua.port = port

        # Asignación del peso neto, cantidad de bultos, unidad comercial, etc
        dua.total_peso_neto = Decimal(
            hxs.select('/html/body/table[1]/tr[14]/td[2]/font/text()').extract()[0].replace(',', '')
            )
        dua.total_cant_bulto = Decimal(
            hxs.select('/html/body/table[1]/tr[15]/td[2]/font/text()').extract()[0].replace(',', '')
            )
        dua.unid_comercial = Decimal(
            hxs.select('/html/body/table[1]/tr[16]/td[2]/font/text()').extract()[0].replace(',', '')
            )
        dua.total_series = int(
            hxs.select('/html/body/table[1]/tr[17]/td[2]/font/text()').extract()[0].replace(',', '')
            )
        dua.total_peso_bruto = Decimal(
            hxs.select('/html/body/table[1]/tr[14]/td[4]/font/text()').extract()[0].replace(',', '')
            )
        dua.total_unid_fisica = Decimal(
            hxs.select('/html/body/table[1]/tr[15]/td[4]/font/text()').extract()[0].replace(',', '')
            )
        dua.tipo_tratamiento = hxs.select('/html/body/table[1]/tr[17]/td[4]/font/text()').extract()[0]
        dua.fob = Decimal(
            hxs.select('/html/body/table[1]/tr[19]/td[3]/font/text()').extract()[0].replace(',', '')
            )
        dua.flete = Decimal(
            hxs.select('/html/body/table[1]/tr[20]/td[3]/font/text()').extract()[0].replace(',', '')
            )
        dua.seguro = Decimal(
            hxs.select('/html/body/table[1]/tr[21]/td[3]/font/text()').extract()[0].replace(',', '')
            )
        dua.cif = Decimal(
            hxs.select('/html/body/table[1]/tr[22]/td[3]/font/text()').extract()[0].replace(',', '')
            )
        dua.ad_valorem = Decimal(
            hxs.select('/html/body/table[1]/tr[25]/td[2]/font/text()').extract()[0].replace(',', '')
            )
        dua.derecho_especifico = Decimal(
            hxs.select('/html/body/table[1]/tr[26]/td[2]/font/text()').extract()[0].replace(',', '')
            )
        dua.imp_select_consumo = Decimal(
            hxs.select('/html/body/table[1]/tr[27]/td[2]/font/text()').extract()[0].replace(',', '')
            )
        dua.imp_promocion_municipal = Decimal(
            hxs.select('/html/body/table[1]/tr[28]/td[2]/font/text()').extract()[0].replace(',', '')
            )
        dua.imp_general_venta = Decimal(
            hxs.select('/html/body/table[1]/tr[29]/td[2]/font/text()').extract()[0].replace(',', '')
            )
        dua.derecho_antidumping = Decimal(
            hxs.select('/html/body/table[1]/tr[30]/td[2]/font/text()').extract()[0].replace(',', '')
            )
        dua.tasa_servicio = Decimal(
            hxs.select('/html/body/table[1]/tr[31]/td[2]/font/text()').extract()[0].replace(',', '')
            )
        dua.recargo_numeracion = Decimal(
            hxs.select('/html/body/table[1]/tr[32]/td[2]/font/text()').extract()[0].replace(',', '')
            )
        dua.sobretasa_natural = Decimal(
            hxs.select('/html/body/table[1]/tr[33]/td[2]/font/text()').extract()[0].replace(',', '')
            )
        dua.ultimo_dia_pago = datetime.strptime(
            hxs.select('/html/body/table[1]/tr[35]/td[2]/font/text()').extract()[0],
            "%d/%m/%Y"
            ).date()
        dua.fecha_cancelacion = datetime.strptime(
            hxs.select('/html/body/table[1]/tr[35]/td[4]/font/text()').extract()[0],
            "%d/%m/%Y"
            ).date()
        dua.fecha_numeracion = datetime.strptime(
            hxs.select('/html/body/table[1]/tr[2]/td[4]/font/text()').extract()[0],
            "%d/%m/%Y"
            ).date()
        dua.banco_cancelacion = hxs.select('/html/body/table[1]/tr[35]/td[6]/font/text()').extract()[0]
        dua.liquidacion = Decimal(
            hxs.select('/html/body/table[1]/tr[34]/td[2]/font/text()').extract()[0].replace(',', '')
            )
        dua.save()

        # create products.
        products_hxs = "/html/body/table[2]/tr[position()>=9]"
        product = hs = hts = detalle_dua = price = None
        line = 1

        for product_rows in hxs.select(products_hxs):
            if product_rows.select("td[1]/@colspan").extract() and \
                product_rows.select("td[1]/@colspan").extract()[0]=="9":
                product = hs = hts = detalle_dua = price = None
                line = 1
                continue

            if line == 1:
                detalle_dua = DetalleDua(dua=dua)
                detalle_dua.guia_aerea_bl = product_rows.select(
                    'td[3]/font/text()').extract()[0]
                detalle_dua.fecha_embarque = datetime.strptime(
                    product_rows.select('td[4]/font/text()').extract()[0],
                    "%d/%m/%Y"
                ).date()
                detalle_dua.decl_pref = product_rows.select(
                    'td[5]/font/text()').extract()[0]
                detalle_dua.item = product_rows.select(
                    'td[6]/font/text()').extract()[0]
                detalle_dua.save()


            elif line == 2:
                detalle_dua.total_cant_bulto = Decimal(
                    product_rows.select('td[2]/font/text()').extract()[0].replace(',', '')
                    )
                detalle_dua.clase = product_rows.select(
                    'td[3]/font/text()').extract()[0]
                detalle_dua.unid_fisicas = product_rows.select(
                    'td[4]/font/text()').extract()[0]
                detalle_dua.peso_neto = Decimal(
                    product_rows.select('td[5]/font/text()').extract()[0].replace(',', '')
                    )
                detalle_dua.peso_bruto = Decimal(
                    product_rows.select('td[6]/font/text()').extract()[0].replace(',', '')
                    )
                detalle_dua.save()

            elif line == 3:
                detalle_dua.flete = Decimal(
                    product_rows.select('td[2]/font/text()').extract()[0].replace(',', '')
                    )
                detalle_dua.seguro = Decimal(product_rows.select(
                    'td[3]/font/text()').extract()[0].replace(',', '')
                    )
                detalle_dua.ad_valorem = Decimal(product_rows.select(
                    'td[4]/font/text()').extract()[0].replace(',', '')
                    )
                detalle_dua.igv = Decimal(
                    product_rows.select('td[5]/font/text()').extract()[0].replace(',', '')
                    )
                detalle_dua.ipm = Decimal(
                    product_rows.select('td[6]/font/text()').extract()[0].replace(',', '')
                    )
                detalle_dua.save()

            elif line == 4:
                detalle_dua.pais_origen = product_rows.select(
                    'td[2]/font/text()').extract()[0]
                detalle_dua.pais_adquision = product_rows.select(
                    'td[3]/font/text()').extract()[0]
                detalle_dua.pais_adquision = product_rows.select(
                    'td[4]/font/text()').extract()[0]
                detalle_dua.trato_pref = product_rows.select(
                    'td[5]/font/text()').extract()[0]
                detalle_dua.cod_liberacion = product_rows.select(
                    'td[6]/font/text()').extract()[0]
                detalle_dua.save()


            elif line == 5:
                detalle_dua.certi_origen = product_rows.select(
                    'td[2]/font/text()').extract()[0]
                detalle_dua.nabandina = product_rows.select(
                    'td[6]/font/text()').extract()[0]
                detalle_dua.save()

            elif line == 6:
                hts_code = product_rows.select('td[2]/font/text()').extract()[0]
                hts_description = product_rows.select('td[3]/font/text()').extract()[0]
                hts, created = HtsItem.django_model.objects.get_or_create(
                    code=hts_code, defaults={'description': hts_description})

            elif line == 7:
                product, created = ProductItem.django_model.objects.get_or_create(
                    name=product_rows.select('td[2]/font/text()').extract()[0],
                    defaults={'hts': hts}
                    )
                detalle_dua.product = product
                detalle_dua.save()

            else:
                prod_desc = product_rows.select('td[2]/font/text()').extract()[0]
                product.description = "%s %s" % (str(product.description), prod_desc)
                detalle_dua.save()
            line += 1

    def dua_container_list(self, response):
        hxs = HtmlXPathSelector(response)
        xpath_container = '/html/body/table[3]/tr[@class="bg"]'
        dua = response.meta['dua']
        for container_hxs in hxs.select(xpath_container):
            container, created = ContainerItem.django_model.objects.get_or_create(
                code=container_hxs.select('td[2]/text()').extract()[0]
                )
            if not dua.containers.filter(code=container.code).count():
                dua.containers.add(container)
                dua.save()


    def dua_formatb(self, response):
        xpath_declaracion_valor = "/html/body/table/tr[2]/td/font/a/@href"
        hxs = HtmlXPathSelector(response)
        url_declaracion_valor = hxs.select(xpath_declaracion_valor).extract()[0]
        return Request(url=self.domain + url_declaracion_valor, callback=self.dua_formatob_declaracion)

    def dua_formatob_declaracion(self, response):
        # Extraer declarante, crear declarante y asociarlo a la dua
        pass