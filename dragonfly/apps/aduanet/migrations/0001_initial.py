# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product'
        db.create_table('aduanet_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hs', self.gf('django.db.models.fields.CharField')(max_length=8)),
        ))
        db.send_create_signal('aduanet', ['Product'])


    def backwards(self, orm):
        # Deleting model 'Product'
        db.delete_table('aduanet_product')


    models = {
        'aduanet.product': {
            'Meta': {'object_name': 'Product'},
            'hs': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['aduanet']