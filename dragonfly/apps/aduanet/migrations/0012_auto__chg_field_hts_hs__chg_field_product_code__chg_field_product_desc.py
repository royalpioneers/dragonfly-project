# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Hts.hs'
        db.alter_column('aduanet_hts', 'hs_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Hs'], null=True))

        # Changing field 'Product.code'
        db.alter_column('aduanet_product', 'code', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'Product.description'
        db.alter_column('aduanet_product', 'description', self.gf('django.db.models.fields.CharField')(max_length=120, null=True))

        # Changing field 'Product.price'
        db.alter_column('aduanet_product', 'price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'DetalleDua.total_cant_bulto'
        db.alter_column('aduanet_detalledua', 'total_cant_bulto', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2))

        # Changing field 'DetalleDua.ipm'
        db.alter_column('aduanet_detalledua', 'ipm', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'DetalleDua.ad_valorem'
        db.alter_column('aduanet_detalledua', 'ad_valorem', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'DetalleDua.unid_comercial'
        db.alter_column('aduanet_detalledua', 'unid_comercial', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=20))

        # Changing field 'DetalleDua.guia_aerea_bl'
        db.alter_column('aduanet_detalledua', 'guia_aerea_bl', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'DetalleDua.peso_bruto'
        db.alter_column('aduanet_detalledua', 'peso_bruto', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'DetalleDua.decl_pref'
        db.alter_column('aduanet_detalledua', 'decl_pref', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'DetalleDua.fob'
        db.alter_column('aduanet_detalledua', 'fob', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=2))

        # Changing field 'DetalleDua.fecha_embarque'
        db.alter_column('aduanet_detalledua', 'fecha_embarque', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'DetalleDua.tipo_uc'
        db.alter_column('aduanet_detalledua', 'tipo_uc', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'DetalleDua.pais_origen'
        db.alter_column('aduanet_detalledua', 'pais_origen', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'DetalleDua.product'
        db.alter_column('aduanet_detalledua', 'product_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Product'], null=True))

        # Changing field 'DetalleDua.clase'
        db.alter_column('aduanet_detalledua', 'clase', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'DetalleDua.moneda_transacc'
        db.alter_column('aduanet_detalledua', 'moneda_transacc', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2))

        # Changing field 'DetalleDua.fech_vencimiento'
        db.alter_column('aduanet_detalledua', 'fech_vencimiento', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'DetalleDua.pais_adquision'
        db.alter_column('aduanet_detalledua', 'pais_adquision', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'DetalleDua.estado'
        db.alter_column('aduanet_detalledua', 'estado', self.gf('django.db.models.fields.CharField')(max_length=4, null=True))

        # Changing field 'DetalleDua.certi_origen'
        db.alter_column('aduanet_detalledua', 'certi_origen', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'DetalleDua.description_partida_cancelaria'
        db.alter_column('aduanet_detalledua', 'description_partida_cancelaria', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'DetalleDua.seguro'
        db.alter_column('aduanet_detalledua', 'seguro', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=2))

        # Changing field 'DetalleDua.item'
        db.alter_column('aduanet_detalledua', 'item', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'DetalleDua.trato_pref'
        db.alter_column('aduanet_detalledua', 'trato_pref', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'DetalleDua.cod_liberacion'
        db.alter_column('aduanet_detalledua', 'cod_liberacion', self.gf('django.db.models.fields.CharField')(max_length=6, null=True))

        # Changing field 'DetalleDua.isc'
        db.alter_column('aduanet_detalledua', 'isc', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'DetalleDua.flete'
        db.alter_column('aduanet_detalledua', 'flete', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2))

        # Changing field 'DetalleDua.unid_fisicas'
        db.alter_column('aduanet_detalledua', 'unid_fisicas', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

    def backwards(self, orm):

        # Changing field 'Hts.hs'
        db.alter_column('aduanet_hts', 'hs_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['aduanet.Hs']))

        # Changing field 'Product.code'
        db.alter_column('aduanet_product', 'code', self.gf('django.db.models.fields.CharField')(default=None, max_length=15))

        # Changing field 'Product.description'
        db.alter_column('aduanet_product', 'description', self.gf('django.db.models.fields.CharField')(default='', max_length=120))

        # Changing field 'Product.price'
        db.alter_column('aduanet_product', 'price', self.gf('django.db.models.fields.DecimalField')(default=None, max_digits=10, decimal_places=2))

        # Changing field 'DetalleDua.total_cant_bulto'
        db.alter_column('aduanet_detalledua', 'total_cant_bulto', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=5, decimal_places=2))

        # Changing field 'DetalleDua.ipm'
        db.alter_column('aduanet_detalledua', 'ipm', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2))

        # Changing field 'DetalleDua.ad_valorem'
        db.alter_column('aduanet_detalledua', 'ad_valorem', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2))

        # Changing field 'DetalleDua.unid_comercial'
        db.alter_column('aduanet_detalledua', 'unid_comercial', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=20, decimal_places=20))

        # Changing field 'DetalleDua.guia_aerea_bl'
        db.alter_column('aduanet_detalledua', 'guia_aerea_bl', self.gf('django.db.models.fields.CharField')(default='', max_length=15))

        # Changing field 'DetalleDua.peso_bruto'
        db.alter_column('aduanet_detalledua', 'peso_bruto', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2))

        # Changing field 'DetalleDua.decl_pref'
        db.alter_column('aduanet_detalledua', 'decl_pref', self.gf('django.db.models.fields.CharField')(default=None, max_length=50))

        # Changing field 'DetalleDua.fob'
        db.alter_column('aduanet_detalledua', 'fob', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=12, decimal_places=2))

        # Changing field 'DetalleDua.fecha_embarque'
        db.alter_column('aduanet_detalledua', 'fecha_embarque', self.gf('django.db.models.fields.CharField')(default=None, max_length=15))

        # Changing field 'DetalleDua.tipo_uc'
        db.alter_column('aduanet_detalledua', 'tipo_uc', self.gf('django.db.models.fields.CharField')(default=None, max_length=15))

        # Changing field 'DetalleDua.pais_origen'
        db.alter_column('aduanet_detalledua', 'pais_origen', self.gf('django.db.models.fields.CharField')(default=None, max_length=50))

        # Changing field 'DetalleDua.product'
        db.alter_column('aduanet_detalledua', 'product_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['aduanet.Product']))

        # Changing field 'DetalleDua.clase'
        db.alter_column('aduanet_detalledua', 'clase', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # Changing field 'DetalleDua.moneda_transacc'
        db.alter_column('aduanet_detalledua', 'moneda_transacc', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=15, decimal_places=2))

        # Changing field 'DetalleDua.fech_vencimiento'
        db.alter_column('aduanet_detalledua', 'fech_vencimiento', self.gf('django.db.models.fields.CharField')(default=None, max_length=15))

        # Changing field 'DetalleDua.pais_adquision'
        db.alter_column('aduanet_detalledua', 'pais_adquision', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'DetalleDua.estado'
        db.alter_column('aduanet_detalledua', 'estado', self.gf('django.db.models.fields.CharField')(default='', max_length=4))

        # Changing field 'DetalleDua.certi_origen'
        db.alter_column('aduanet_detalledua', 'certi_origen', self.gf('django.db.models.fields.CharField')(default=None, max_length=20))

        # Changing field 'DetalleDua.description_partida_cancelaria'
        db.alter_column('aduanet_detalledua', 'description_partida_cancelaria', self.gf('django.db.models.fields.CharField')(default=None, max_length=100))

        # Changing field 'DetalleDua.seguro'
        db.alter_column('aduanet_detalledua', 'seguro', self.gf('django.db.models.fields.CharField')(default=None, max_length=50))

        # Changing field 'DetalleDua.item'
        db.alter_column('aduanet_detalledua', 'item', self.gf('django.db.models.fields.CharField')(default=None, max_length=50))

        # Changing field 'DetalleDua.trato_pref'
        db.alter_column('aduanet_detalledua', 'trato_pref', self.gf('django.db.models.fields.DecimalField')(default=None, max_digits=8, decimal_places=2))

        # Changing field 'DetalleDua.cod_liberacion'
        db.alter_column('aduanet_detalledua', 'cod_liberacion', self.gf('django.db.models.fields.CharField')(default=None, max_length=6))

        # Changing field 'DetalleDua.isc'
        db.alter_column('aduanet_detalledua', 'isc', self.gf('django.db.models.fields.DecimalField')(default=None, max_digits=10, decimal_places=2))

        # Changing field 'DetalleDua.flete'
        db.alter_column('aduanet_detalledua', 'flete', self.gf('django.db.models.fields.DecimalField')(default=None, max_digits=8, decimal_places=2))

        # Changing field 'DetalleDua.unid_fisicas'
        db.alter_column('aduanet_detalledua', 'unid_fisicas', self.gf('django.db.models.fields.CharField')(default=None, max_length=20))

    models = {
        'aduanet.aduana': {
            'Meta': {'object_name': 'Aduana'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'aduanet.agent': {
            'Meta': {'object_name': 'Agent'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        'aduanet.container': {
            'Meta': {'object_name': 'Container'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'aduanet.country': {
            'Meta': {'object_name': 'Country'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'aduanet.declarante': {
            'Meta': {'object_name': 'Declarante'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'aduanet.detalledua': {
            'Meta': {'object_name': 'DetalleDua'},
            'ad_valorem': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'certi_origen': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'clase': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'cod_liberacion': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'decl_pref': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'description_partida_cancelaria': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'dua': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Dua']"}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'fech_vencimiento': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'fecha_embarque': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'flete': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'fob': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'guia_aerea_bl': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ipm': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'isc': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'item': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'moneda_transacc': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'pais_adquision': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'pais_origen': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'peso_bruto': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Product']", 'null': 'True', 'blank': 'True'}),
            'seguro': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'tipo_uc': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'total_cant_bulto': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'trato_pref': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'unid_comercial': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '20', 'blank': 'True'}),
            'unid_fisicas': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        'aduanet.dua': {
            'Meta': {'object_name': 'Dua'},
            'ad_valorem': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'aduana': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Aduana']", 'null': 'True', 'blank': 'True'}),
            'agent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Agent']", 'null': 'True', 'blank': 'True'}),
            'banco_cancelacion': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'cif': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'containers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['aduanet.Container']", 'null': 'True', 'blank': 'True'}),
            'declarante': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Declarante']", 'null': 'True', 'blank': 'True'}),
            'derecho_antidumping': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'derecho_especifico': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'fecha_cancelacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_llegada': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_numeracion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'flete': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'fob': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp_general_venta': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'imp_promocion_municipal': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'imp_select_consumo': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'importer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Importer']", 'null': 'True', 'blank': 'True'}),
            'liquidacion': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'port': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Port']", 'null': 'True', 'blank': 'True'}),
            'recargo_numeracion': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'regime': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Regime']", 'null': 'True', 'blank': 'True'}),
            'seguro': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'sobretasa_natural': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Status']", 'null': 'True', 'blank': 'True'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Supplier']", 'null': 'True', 'blank': 'True'}),
            'tasa_servicio': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'tipo_tratamiento': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'total_cant_bulto': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'total_peso_bruto': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'total_peso_neto': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'total_series': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_unid_fisica': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'transport': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Transport']", 'null': 'True', 'blank': 'True'}),
            'ultimo_dia_pago': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'unid_comercial': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2', 'blank': 'True'})
        },
        'aduanet.hs': {
            'Meta': {'object_name': 'Hs'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'aduanet.hts': {
            'Meta': {'object_name': 'Hts'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'hs': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Hs']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'aduanet.importer': {
            'Meta': {'object_name': 'Importer'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'aduanet.port': {
            'Meta': {'object_name': 'Port'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'aduanet.product': {
            'Meta': {'object_name': 'Product'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'hts': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Hts']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'})
        },
        'aduanet.regime': {
            'Meta': {'object_name': 'Regime'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'aduanet.status': {
            'Meta': {'object_name': 'Status'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'aduanet.supplier': {
            'Meta': {'object_name': 'Supplier'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'aduanet.transport': {
            'Meta': {'object_name': 'Transport'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['aduanet']