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

   class Meta:
        verbose_name = u"Régimen"
        verbose_name_plural = u"Regímenes"

   def __unicode__(self):
        return "%s - %s" % (self.code, self.name)

class Aduana(models.Model):
   code = models.CharField(max_length=10)
   name = models.CharField(max_length=150)

   class Meta:
        verbose_name = u"Aduana"
        verbose_name_plural = u"Aduanas"

   def __unicode__(self):
        return "%s - %s" % (self.code, self.name)

class Agent(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=120)

    class Meta:
        verbose_name = u"Agente"
        verbose_name_plural = u"Agentes"

    def __unicode__(self):
        return "%s - %s" % (self.code, self.name)

class Container(models.Model):
    code = models.CharField(max_length=20)

    class Meta:
        verbose_name = u"Contenedor"
        verbose_name_plural = u"Contenedores"

    def __unicode__(self):
        return self.code

class Supplier(models.Model):
    code = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=70)
    fax = models.CharField(max_length=20)

    class Meta:
        verbose_name = u"Provedor"
        verbose_name_plural = u"Proveedores"

    def __unicode__(self):
        return "%s" % (self.code, )

class Port(models.Model):
    code =  models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = u"Puerto"
        verbose_name_plural = u"Puertos"

    def __unicode__(self):
        return "%s - %s" % (self.code, self.name)

class Importer(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    address =  models.CharField(max_length=300)

    class Meta:
        verbose_name = u"Importador"
        verbose_name_plural = u"Importadores"

    def __unicode__(self):
        return "%s - %s" % (self.code, self.name)

class Declarante(models.Model): 
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)

    class Meta:
        verbose_name = u"Declarante"
        verbose_name_plural = u"Declarantes"

    def __unicode__(self):
        return "%s - %s %s" % (self.code, self.name, self.apellido)

class Status(models.Model):
    code =  models.CharField(max_length=10)
    tipo = models.CharField(max_length=15)
    description = models.CharField(max_length=100)

class Transport (models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=100)

    #class Meta:
    #    verbose_name = u""
    #    verbose_name_plural = u""

###### En esta clase falta como se va a guardar la fecha
class Dua (models.Model):
    code =  models.CharField(max_length=21)
    regime = models.ForeignKey('Regime', blank=True, null=True)
    aduana =  models.ForeignKey('Aduana', blank=True, null=True)
    agent =  models.ForeignKey('Agent', blank=True, null=True)
    transport = models.ForeignKey('Transport', blank=True, null=True)
    importer = models.ForeignKey('Importer', blank=True, null=True)
    supplier = models.ForeignKey('Supplier', blank=True, null=True)
    fecha_llegada = models.DateField(blank=True, null=True)
    status = models.ForeignKey('Status', blank=True, null=True)
    port = models.ForeignKey('Port', blank=True, null=True)
    total_peso_neto = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    total_cant_bulto = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    unid_comercial = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    total_series = models.IntegerField(blank=True, null=True)
    total_peso_bruto = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    total_unid_fisica = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tipo_tratamiento = models.CharField(max_length=50, blank=True, null=True)
    fob =  models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    flete =  models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    seguro = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ad_valorem = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    cif = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    derecho_especifico = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    imp_select_consumo = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    imp_promocion_municipal= models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    imp_general_venta = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    derecho_antidumping = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tasa_servicio = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    recargo_numeracion = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    sobretasa_natural = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ultimo_dia_pago = models.DateField(blank=True, null=True)
    fecha_cancelacion = models.DateField(blank=True, null=True)
    fecha_numeracion = models.DateField(blank=True, null=True)
    banco_cancelacion = models.CharField(max_length=50, blank=True, null=True)
    liquidacion = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    declarante = models.ForeignKey('Declarante', blank=True, null=True)
    containers=models.ManyToManyField('Container', blank=True, null=True)

    def __unicode__(self):
        return self.code

    class Meta:
        verbose_name = u"DUA"
        verbose_name_plural = u"DUAs"

class Hs(models.Model):
    code = models.CharField(max_length=15)

    class Meta:
        verbose_name = u"HS"
        verbose_name_plural = u"HS"

    def __unicode__(self):
        return u"%s" % (self.code, )

class Hts(models.Model):
    code = models.CharField(max_length=15)
    description = models.CharField(max_length=200)
    hs = models.ForeignKey('Hs', blank=True, null=True)
    nabandina =  models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        verbose_name = u"HTS"
        verbose_name_plural = u"HTS"

    def __unicode__(self):
        return u"%s" % (self.code, )

class Product(models.Model):
    code = models.CharField(max_length=15, blank=True, null=True)
    hts = models.ForeignKey('Hts')
    name = models.CharField(max_length=100)
    description =  models.CharField(max_length=120, default="", blank=True, null=True)
    # Precios calculados
    precio_cif = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    precio_fob = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    precio_total = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    precio_regulado = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    precio_cif_uf = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    precio_fob_uf = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    precio_total_uf = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    precio_regulado_uf = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)


    class Meta:
        verbose_name = u"Producto"
        verbose_name_plural = u"Productos"

    def __unicode__(self):
        return u"%s - %s" % (self.code, self.name)

class DetalleDua(models.Model):
    dua = models.ForeignKey('Dua')
    product = models.ForeignKey('Product', blank=True, null=True)
    total_cant_bulto=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    flete = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    pais_origen = models.CharField(max_length=50, blank=True, null=True)
    guia_aerea_bl=models.CharField(max_length=200, blank=True, null=True)
    clase = models.CharField(max_length=60, blank=True, null=True)
    seguro = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    pais_adquision = models.CharField(max_length=50, blank=True, null=True)
    description_partida_cancelaria = models.CharField(max_length=100, blank=True, null=True)
    fecha_embarque=models.DateField(blank=True, null=True)
    unid_fisicas = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    tipo_unid_fisicas = models.CharField(max_length=10, blank=True, null=True)
    ad_valorem = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    igv = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    trato_pref_int = models.CharField(max_length=10, blank=True, null=True)
    trato_pref_nac = models.CharField(max_length=10, blank=True, null=True)
    decl_pref = models.CharField(max_length=50, blank=True, null=True)
    item =  models.CharField(max_length=50, blank=True, null=True)    
    peso_bruto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    peso_neto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ipm = models.DecimalField(max_digits=10,decimal_places=2, blank=True, null=True)
    cod_liberacion = models.CharField(max_length=200, blank=True, null=True)
    fech_vencimiento = models.DateField(blank=True, null=True)
    moneda_transacc =  models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    isc =  models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    certi_origen = models.CharField(max_length=20, blank=True, null=True)
    fob = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    estado = models.CharField(max_length=15, blank=True, null=True)
    unid_comercial = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    tipo_uc = models.CharField(max_length=15, blank=True, null=True)

    
    class Meta:
        verbose_name = u"Detalle DUA"
        verbose_name_plural = u"Detalle DUAs"

    def __unicode__(self):
        return "%s - %s" % (self.dua.code, self.product.code)


