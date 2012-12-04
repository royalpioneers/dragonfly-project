# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from aduanet.models import Product

class ProductPipeline(object):
    def process_item(self, item, spider):
        item.save()
        return item
