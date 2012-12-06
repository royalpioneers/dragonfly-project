# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Importer'
        db.create_table('aduanet_importer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal('aduanet', ['Importer'])

        # Adding model 'Hts'
        db.create_table('aduanet_hts', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('hs', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Hs'])),
        ))
        db.send_create_signal('aduanet', ['Hts'])

        # Adding model 'Declarante'
        db.create_table('aduanet_declarante', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cargo', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('aduanet', ['Declarante'])

        # Adding model 'Port'
        db.create_table('aduanet_port', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('aduanet', ['Port'])

        # Adding model 'Status'
        db.create_table('aduanet_status', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('aduanet', ['Status'])

        # Adding model 'Product'
        db.create_table('aduanet_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('hts', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Hts'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal('aduanet', ['Product'])

        # Adding model 'DetalleDua'
        db.create_table('aduanet_detalledua', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dua', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Dua'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Product'])),
            ('total_cant_bulto', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('flete', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('pais_origen', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('guia_aerea_bl', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('clase', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('seguro', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pais_adquision', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description_partida_cancelaria', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('fecha_embarque', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('unid_fisicas', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('ad_valorem', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('trato_pref', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('decl_pref', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('item', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('peso_bruto', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('ipm', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('cod_liberacion', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('fech_vencimiento', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('moneda_transacc', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('isc', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('certi_origen', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('fob', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('unid_comercial', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=20)),
            ('tipo_uc', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('aduanet', ['DetalleDua'])

        # Adding model 'Transport'
        db.create_table('aduanet_transport', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('aduanet', ['Transport'])

        # Adding model 'Hs'
        db.create_table('aduanet_hs', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('aduanet', ['Hs'])

        # Adding model 'Supplier'
        db.create_table('aduanet_supplier', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('aduanet', ['Supplier'])

        # Adding model 'Dua'
        db.create_table('aduanet_dua', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('regime', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Regime'])),
            ('aduana', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Aduana'])),
            ('agent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Agent'])),
            ('transport', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Transport'])),
            ('importer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Importer'])),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Supplier'])),
            ('fecha_llegada', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Status'])),
            ('port', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Port'])),
            ('total_peso_neto', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('total_cant_bulto', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('unid_comercial', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=20)),
            ('total_series', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('total_peso_bruto', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('total_unid_fisica', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('res_exo_num', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('tipo_tratamiento', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('fob', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('flete', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('seguro', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('ad_valorem', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('derecho_especifico', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('imp_select_consumo', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('imp_promocion_municipal', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('imp_general_venta', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('derecho_antidumping', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('tasa_servicio', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('recargo_numeracion', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('sobretasa_natural', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('ultimo_dia_pago', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('fecha_cancelacion', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('fecha_numeracion', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('banco_cancelacion', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('liquidacion', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('declarante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Declarante'])),
        ))
        db.send_create_signal('aduanet', ['Dua'])

        # Adding M2M table for field containers on 'Dua'
        db.create_table('aduanet_dua_containers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dua', models.ForeignKey(orm['aduanet.dua'], null=False)),
            ('container', models.ForeignKey(orm['aduanet.container'], null=False))
        ))
        db.create_unique('aduanet_dua_containers', ['dua_id', 'container_id'])

        # Adding model 'Container'
        db.create_table('aduanet_container', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=12)),
        ))
        db.send_create_signal('aduanet', ['Container'])


    def backwards(self, orm):
        # Deleting model 'Importer'
        db.delete_table('aduanet_importer')

        # Deleting model 'Hts'
        db.delete_table('aduanet_hts')

        # Deleting model 'Declarante'
        db.delete_table('aduanet_declarante')

        # Deleting model 'Port'
        db.delete_table('aduanet_port')

        # Deleting model 'Status'
        db.delete_table('aduanet_status')

        # Deleting model 'Product'
        db.delete_table('aduanet_product')

        # Deleting model 'DetalleDua'
        db.delete_table('aduanet_detalledua')

        # Deleting model 'Transport'
        db.delete_table('aduanet_transport')

        # Deleting model 'Hs'
        db.delete_table('aduanet_hs')

        # Deleting model 'Supplier'
        db.delete_table('aduanet_supplier')

        # Deleting model 'Dua'
        db.delete_table('aduanet_dua')

        # Removing M2M table for field containers on 'Dua'
        db.delete_table('aduanet_dua_containers')

        # Deleting model 'Container'
        db.delete_table('aduanet_container')


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
            'ad_valorem': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'aduana': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Aduana']"}),
            'agent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Agent']"}),
            'banco_cancelacion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'containers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['aduanet.Container']", 'symmetrical': 'False'}),
            'declarante': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Declarante']"}),
            'derecho_antidumping': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'derecho_especifico': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'fecha_cancelacion': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'fecha_llegada': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'fecha_numeracion': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'flete': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'fob': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp_general_venta': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'imp_promocion_municipal': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'imp_select_consumo': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'importer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Importer']"}),
            'liquidacion': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'port': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Port']"}),
            'recargo_numeracion': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'regime': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Regime']"}),
            'res_exo_num': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'seguro': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'sobretasa_natural': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Status']"}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Supplier']"}),
            'tasa_servicio': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'tipo_tratamiento': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'total_cant_bulto': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'total_peso_bruto': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'total_peso_neto': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'total_series': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'total_unid_fisica': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'transport': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Transport']"}),
            'ultimo_dia_pago': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'unid_comercial': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '20'})
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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