# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field
from scrapy.contrib_exp.djangoitem import DjangoItem
from aduanet.models import Country, Regime, Aduana, Agent, Container, \
Supplier, Port, Importer, Declarante, Status, Transport, Dua, \
Hs, Hts, Product, DetalleDua, CountryProduct

class CountryItem(DjangoItem):
	django_model = Country

class RegimeItem(DjangoItem):
	django_model = Regime

class AduanaItem(DjangoItem):
	django_model = Aduana

class AgentItem(DjangoItem):
	django_model = Agent

class ContainerItem(DjangoItem):
	django_model = Container

class SupplierItem(DjangoItem):
	django_model = Supplier 

class PortItem(DjangoItem):
	django_model = Port

class ImporterItem(DjangoItem):
	django_model = Importer

class DeclaranteItem(DjangoItem):
	django_model = Declarante

class StatusItem(DjangoItem):
	django_model = Status

class TransportItem(DjangoItem):
	django_model = Transport

class DuaItem(DjangoItem):
	django_model = Dua

class HsItem(DjangoItem):
	django_model = Hs

class HtsItem(DjangoItem):
	django_model = Hts

class CountryProductItem(DjangoItem):
	django_model = CountryProduct

class ProductItem(DjangoItem):
	django_model = Product

class DetalleDuaItem(DjangoItem):
	django_model = DetalleDua


    