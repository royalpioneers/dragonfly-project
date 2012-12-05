from django.contrib import admin
from aduanet.models import Country, Regime, Aduana

#class ProductAdmin(admin.ModelAdmin):
#    pass

admin.site.register(Country)
admin.site.register(Regime)
admin.site.register(Aduana)