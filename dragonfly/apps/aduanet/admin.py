from django.contrib import admin
from aduanet.models import Country, Regime, Aduana, Agent

#class ProductAdmin(admin.ModelAdmin):
#    pass

admin.site.register(Country)
admin.site.register(Regime)
admin.site.register(Aduana)
admin.site.register(Agent)