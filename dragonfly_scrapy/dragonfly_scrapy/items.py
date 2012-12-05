# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field
from scrapy.contrib_exp.djangoitem import DjangoItem
from aduanet.models import Country, Regime, Aduana

class CountryItem(DjangoItem):
	django_model = Country

class RegimeItem(DjangoItem):
	django_model = Regime

class AduanaItem(DjangoItem):
	django_model = Aduana