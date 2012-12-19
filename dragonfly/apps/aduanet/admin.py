from django.contrib import admin
from django.db.models import Count
#from django.contrib.admin.filterspecs import FilterSpec, RelatedFilterSpec
from aduanet.models import Country, Regime, Aduana, Agent, Container, \
    Supplier, Port, Importer, Declarante, Status, Transport, Dua, \
    Hs, Hts, Product, DetalleDua

class HtsListFilter(admin.SimpleListFilter):
    title = 'HTS'
    parameter_name = 'hts'

    def lookups(self, request, model_admin):
        search_words = request.GET.get('q', '')
        hts_list = Hts.objects.filter(
            product__name__icontains=search_words
            ).values('code', 'description').order_by().annotate(Count('code'))

        list = []
        for hts_item in hts_list:
            list.append(
                (hts_item['code'], '%s(%s)' % (hts_item['description'], hts_item['code__count']))
                )
        return list    

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(hts__code__in=self.value().split(','))


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'precio_total', 'precio_regulado')
    search_fields = ['name']
    list_filter = (HtsListFilter,)

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
admin.site.register(Product, ProductAdmin)
admin.site.register(DetalleDua)
