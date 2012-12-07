# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Dua.ultimo_dia_pago'
        db.alter_column('aduanet_dua', 'ultimo_dia_pago', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Dua.fecha_numeracion'
        db.alter_column('aduanet_dua', 'fecha_numeracion', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Dua.fecha_cancelacion'
        db.alter_column('aduanet_dua', 'fecha_cancelacion', self.gf('django.db.models.fields.DateField')(null=True))

    def backwards(self, orm):

        # Changing field 'Dua.ultimo_dia_pago'
        db.alter_column('aduanet_dua', 'ultimo_dia_pago', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

        # Changing field 'Dua.fecha_numeracion'
        db.alter_column('aduanet_dua', 'fecha_numeracion', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

        # Changing field 'Dua.fecha_cancelacion'
        db.alter_column('aduanet_dua', 'fecha_cancelacion', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

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
            'ad_valorem': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'certi_origen': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'clase': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'cod_liberacion': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'decl_pref': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description_partida_cancelaria': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'dua': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Dua']"}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'fech_vencimiento': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'fecha_embarque': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'flete': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'fob': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'guia_aerea_bl': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ipm': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'isc': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'item': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'moneda_transacc': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'pais_adquision': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pais_origen': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'peso_bruto': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Product']"}),
            'seguro': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tipo_uc': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'total_cant_bulto': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'trato_pref': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'unid_comercial': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '20'}),
            'unid_fisicas': ('django.db.models.fields.CharField', [], {'max_length': '20'})
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
            'hs': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Hs']"}),
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
            'code': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'hts': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Hts']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
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