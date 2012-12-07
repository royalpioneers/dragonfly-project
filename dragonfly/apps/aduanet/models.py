# -*- coding: utf-8 -*-
from django.db import models

class Country (models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = u"País"
        verbose_name_plural = u"Países"

    def __unicode__(self):
        return "%s - %s" % (self.code, self.name)

class Regime(models.Model):
   code = models.CharField(max_length = 5)
   name = models.CharField(max_length = 30)

   def __unicode__(self):
        return "%s - %s" % (self.code, self.name)

class Aduana(models.Model):
   code = models.CharField(max_length=10)
   name = models.CharField(max_length=150)

   def __unicode__(self):
        return "%s - %s" % (self.code, self.name)

class Agent(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=120)

    def __unicode__(self):
        return "%s - %s" % (self.code, self.name)

class Container(models.Model):
    code = models.CharField(max_length=12)

    def __unicode__(self):
        return self.code

class Supplier(models.Model):
    code = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=70)
    fax = models.CharField(max_length=20)

class Port(models.Model):
    code =  models.CharField(max_length=10)
    name = models.CharField(max_length=100)

class Importer(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    address =  models.CharField(max_length=120)

    def __unicode__(self):
        return "%s - %s" % (self.code, self.name)

class Declarante(models.Model): 
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)

class Status(models.Model):
    code =  models.CharField(max_length=10)
    tipo = models.CharField(max_length=15)
    description = models.CharField(max_length=100)

class Transport (models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=100)

###### En esta clase falta como se va a guardar la fecha
class Dua (models.Model):
    code =  models.CharField(max_length=15)
    regime = models.ForeignKey('Regime', blank=True, null=True)
    aduana =  models.ForeignKey('Aduana', blank=True, null=True)
    agent =  models.ForeignKey('Agent', blank=True, null=True)
    transport = models.ForeignKey('Transport', blank=True, null=True)
    importer = models.ForeignKey('Importer', blank=True, null=True)
    supplier = models.ForeignKey('Supplier', blank=True, null=True)
    fecha_llegada = models.DateField(blank=True, null=True)
    status = models.ForeignKey('Status', blank=True, null=True)
    port = models.ForeignKey('Port', blank=True, null=True)
    total_peso_neto = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    total_cant_bulto = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    unid_comercial = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    total_series = models.IntegerField(blank=True, null=True)
    total_peso_bruto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_unid_fisica = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tipo_tratamiento = models.CharField(max_length=50, blank=True, null=True)
    fob =  models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    flete =  models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    seguro = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ad_valorem = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cif = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    derecho_especifico = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    imp_select_consumo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    imp_promocion_municipal= models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    imp_general_venta = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    derecho_antidumping = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    tasa_servicio = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    recargo_numeracion = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    sobretasa_natural = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ultimo_dia_pago = models.DateField(blank=True, null=True)
    fecha_cancelacion = models.DateField(blank=True, null=True)
    fecha_numeracion = models.DateField(blank=True, null=True)
    banco_cancelacion = models.CharField(max_length=50, blank=True, null=True)
    liquidacion = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    declarante = models.ForeignKey('Declarante', blank=True, null=True)
    containers=models.ManyToManyField('Container', blank=True, null=True)

    def __unicode__(self):
        return self.code

class Hs(models.Model):
    code = models.CharField(max_length=15)

class Hts(models.Model):
    code = models.CharField(max_length=15)
    hs = models.ForeignKey('Hs')

class Product(models.Model):
    code = models.CharField(max_length=15)
    hts = models.ForeignKey('Hts')
    name = models.CharField(max_length=100)
    description =  models.CharField(max_length=120)
    price =  models.DecimalField(max_digits=10, decimal_places=2)



class DetalleDua(models.Model):
    dua = models.ForeignKey('Dua')
    product = models.ForeignKey('Product')
    total_cant_bulto=models.DecimalField(max_digits=5, decimal_places=2)
    flete = models.DecimalField(max_digits=8, decimal_places=2)
    pais_origen = models.CharField(max_length=50)
    guia_aerea_bl=models.CharField(max_length=15)
    clase = models.CharField(max_length=60)
    seguro = models.CharField(max_length=50)
    pais_adquision = models.CharField(max_length=50)
    description_partida_cancelaria = models.CharField(max_length=100)
    fecha_embarque=models.CharField(max_length=15)
    unid_fisicas = models.CharField(max_length=20)
    ad_valorem = models.DecimalField(max_digits=10, decimal_places=2)
    trato_pref = models.DecimalField(max_digits=8, decimal_places=2)
    decl_pref = models.CharField(max_length=50)
    item =  models.CharField(max_length=50)
    peso_bruto = models.DecimalField(max_digits=10, decimal_places=2)
    ipm = models.DecimalField(max_digits=10,decimal_places=2)
    cod_liberacion = models.CharField(max_length=6)
    fech_vencimiento = models.CharField(max_length=15)
    moneda_transacc =  models.DecimalField(max_digits=15, decimal_places=2)
    isc =  models.DecimalField(max_digits=10, decimal_places=2)
    certi_origen = models.CharField(max_length=20)
    fob = models.DecimalField(max_digits=12, decimal_places=2)
    estado = models.CharField(max_length=4)
    unid_comercial = models.DecimalField(max_digits=20, decimal_places=20)
    tipo_uc = models.CharField(max_length=15)
    


