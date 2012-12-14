# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table('aduanet_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('aduanet', ['Country'])

        # Adding model 'Regime'
        db.create_table('aduanet_regime', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('aduanet', ['Regime'])

        # Adding model 'Aduana'
        db.create_table('aduanet_aduana', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('aduanet', ['Aduana'])

        # Adding model 'Agent'
        db.create_table('aduanet_agent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal('aduanet', ['Agent'])

        # Adding model 'Container'
        db.create_table('aduanet_container', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('aduanet', ['Container'])

        # Adding model 'Supplier'
        db.create_table('aduanet_supplier', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('aduanet', ['Supplier'])

        # Adding model 'Port'
        db.create_table('aduanet_port', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('aduanet', ['Port'])

        # Adding model 'Importer'
        db.create_table('aduanet_importer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('aduanet', ['Importer'])

        # Adding model 'Declarante'
        db.create_table('aduanet_declarante', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cargo', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('aduanet', ['Declarante'])

        # Adding model 'Status'
        db.create_table('aduanet_status', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('aduanet', ['Status'])

        # Adding model 'Transport'
        db.create_table('aduanet_transport', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('aduanet', ['Transport'])

        # Adding model 'Dua'
        db.create_table('aduanet_dua', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=21)),
            ('regime', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Regime'], null=True, blank=True)),
            ('aduana', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Aduana'], null=True, blank=True)),
            ('agent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Agent'], null=True, blank=True)),
            ('transport', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Transport'], null=True, blank=True)),
            ('importer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Importer'], null=True, blank=True)),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Supplier'], null=True, blank=True)),
            ('fecha_llegada', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Status'], null=True, blank=True)),
            ('port', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Port'], null=True, blank=True)),
            ('total_peso_neto', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_cant_bulto', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('unid_comercial', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_series', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('total_peso_bruto', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_unid_fisica', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('tipo_tratamiento', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('fob', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('flete', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('seguro', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('ad_valorem', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('cif', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('derecho_especifico', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('imp_select_consumo', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('imp_promocion_municipal', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('imp_general_venta', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('derecho_antidumping', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('tasa_servicio', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('recargo_numeracion', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('sobretasa_natural', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('ultimo_dia_pago', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fecha_cancelacion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fecha_numeracion', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('banco_cancelacion', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('liquidacion', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('declarante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Declarante'], null=True, blank=True)),
        ))
        db.send_create_signal('aduanet', ['Dua'])

        # Adding M2M table for field containers on 'Dua'
        db.create_table('aduanet_dua_containers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dua', models.ForeignKey(orm['aduanet.dua'], null=False)),
            ('container', models.ForeignKey(orm['aduanet.container'], null=False))
        ))
        db.create_unique('aduanet_dua_containers', ['dua_id', 'container_id'])

        # Adding model 'Hs'
        db.create_table('aduanet_hs', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('aduanet', ['Hs'])

        # Adding model 'Hts'
        db.create_table('aduanet_hts', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('hs', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Hs'], null=True, blank=True)),
            ('nabandina', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
        ))
        db.send_create_signal('aduanet', ['Hts'])

        # Adding model 'Product'
        db.create_table('aduanet_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('hts', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Hts'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=120, null=True, blank=True)),
            ('precio_cif', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2, blank=True)),
            ('precio_fob', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2, blank=True)),
            ('precio_total', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2, blank=True)),
            ('precio_regulado', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2, blank=True)),
            ('precio_cif_uf', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2, blank=True)),
            ('precio_fob_uf', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2, blank=True)),
            ('precio_total_uf', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2, blank=True)),
            ('precio_regulado_uf', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2, blank=True)),
        ))
        db.send_create_signal('aduanet', ['Product'])

        # Adding model 'DetalleDua'
        db.create_table('aduanet_detalledua', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dua', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Dua'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aduanet.Product'], null=True, blank=True)),
            ('total_cant_bulto', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('flete', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True)),
            ('pais_origen', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('guia_aerea_bl', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('clase', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('seguro', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=2, blank=True)),
            ('pais_adquision', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('description_partida_cancelaria', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('fecha_embarque', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('unid_fisicas', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2, blank=True)),
            ('tipo_unid_fisicas', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('ad_valorem', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('igv', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('trato_pref_int', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('trato_pref_nac', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('decl_pref', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('item', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('peso_bruto', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('peso_neto', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('ipm', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('cod_liberacion', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('fech_vencimiento', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('moneda_transacc', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('isc', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('certi_origen', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('fob', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=2, blank=True)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('unid_comercial', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=20, decimal_places=2, blank=True)),
            ('tipo_uc', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
        ))
        db.send_create_signal('aduanet', ['DetalleDua'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table('aduanet_country')

        # Deleting model 'Regime'
        db.delete_table('aduanet_regime')

        # Deleting model 'Aduana'
        db.delete_table('aduanet_aduana')

        # Deleting model 'Agent'
        db.delete_table('aduanet_agent')

        # Deleting model 'Container'
        db.delete_table('aduanet_container')

        # Deleting model 'Supplier'
        db.delete_table('aduanet_supplier')

        # Deleting model 'Port'
        db.delete_table('aduanet_port')

        # Deleting model 'Importer'
        db.delete_table('aduanet_importer')

        # Deleting model 'Declarante'
        db.delete_table('aduanet_declarante')

        # Deleting model 'Status'
        db.delete_table('aduanet_status')

        # Deleting model 'Transport'
        db.delete_table('aduanet_transport')

        # Deleting model 'Dua'
        db.delete_table('aduanet_dua')

        # Removing M2M table for field containers on 'Dua'
        db.delete_table('aduanet_dua_containers')

        # Deleting model 'Hs'
        db.delete_table('aduanet_hs')

        # Deleting model 'Hts'
        db.delete_table('aduanet_hts')

        # Deleting model 'Product'
        db.delete_table('aduanet_product')

        # Deleting model 'DetalleDua'
        db.delete_table('aduanet_detalledua')


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
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
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
            'cod_liberacion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'decl_pref': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'description_partida_cancelaria': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'dua': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Dua']"}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'fech_vencimiento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_embarque': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'flete': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'fob': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'guia_aerea_bl': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'igv': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'ipm': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'isc': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'item': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'moneda_transacc': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'pais_adquision': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'pais_origen': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'peso_bruto': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'peso_neto': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Product']", 'null': 'True', 'blank': 'True'}),
            'seguro': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'tipo_uc': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'tipo_unid_fisicas': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'total_cant_bulto': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'trato_pref_int': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'trato_pref_nac': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'unid_comercial': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2', 'blank': 'True'}),
            'unid_fisicas': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2', 'blank': 'True'})
        },
        'aduanet.dua': {
            'Meta': {'object_name': 'Dua'},
            'ad_valorem': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'aduana': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Aduana']", 'null': 'True', 'blank': 'True'}),
            'agent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Agent']", 'null': 'True', 'blank': 'True'}),
            'banco_cancelacion': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'cif': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '21'}),
            'containers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['aduanet.Container']", 'null': 'True', 'blank': 'True'}),
            'declarante': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Declarante']", 'null': 'True', 'blank': 'True'}),
            'derecho_antidumping': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'derecho_especifico': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'fecha_cancelacion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_llegada': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_numeracion': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'flete': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'fob': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imp_general_venta': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'imp_promocion_municipal': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'imp_select_consumo': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'importer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Importer']", 'null': 'True', 'blank': 'True'}),
            'liquidacion': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'port': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Port']", 'null': 'True', 'blank': 'True'}),
            'recargo_numeracion': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'regime': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Regime']", 'null': 'True', 'blank': 'True'}),
            'seguro': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'sobretasa_natural': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Status']", 'null': 'True', 'blank': 'True'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Supplier']", 'null': 'True', 'blank': 'True'}),
            'tasa_servicio': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'tipo_tratamiento': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'total_cant_bulto': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_peso_bruto': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_peso_neto': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_series': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_unid_fisica': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'transport': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aduanet.Transport']", 'null': 'True', 'blank': 'True'}),
            'ultimo_dia_pago': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'unid_comercial': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'})
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nabandina': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        'aduanet.importer': {
            'Meta': {'object_name': 'Importer'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
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
            'precio_cif': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2', 'blank': 'True'}),
            'precio_cif_uf': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2', 'blank': 'True'}),
            'precio_fob': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2', 'blank': 'True'}),
            'precio_fob_uf': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2', 'blank': 'True'}),
            'precio_regulado': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2', 'blank': 'True'}),
            'precio_regulado_uf': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2', 'blank': 'True'}),
            'precio_total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2', 'blank': 'True'}),
            'precio_total_uf': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2', 'blank': 'True'})
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