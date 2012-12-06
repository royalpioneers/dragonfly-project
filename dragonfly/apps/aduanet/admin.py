from django.contrib import admin
from aduanet.models import Country, Regime, Aduana, Agent, Container, \
	Supplier, Port, Importer, Declarante, Status, Transport, Dua, \
	Hs, Hts, Product, DetalleDua

#class ProductAdmin(admin.ModelAdmin):
#    pass

admin.site.register(Country)
admin.site.register(Regime)
admin.site.register(Aduana)
admin.site.register(Agent)
admin.site.register(Container)
admin.site.register(Supplier)
admin.site.register(Port)
admin.site.register(Importer)
admin.site.register(Declarante)
admin.site.register(Status)
admin.site.register(Transport)
admin.site.register(Dua)
admin.site.register(Hs)
admin.site.register(Hts)
admin.site.register(Product)
admin.site.register(DetalleDua)
