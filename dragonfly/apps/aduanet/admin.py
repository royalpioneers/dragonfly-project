from django.contrib import admin
from aduanet.models import Product

#class ProductAdmin(admin.ModelAdmin):
#    pass

admin.site.register(Product)