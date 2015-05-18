# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Quoter'
        db.create_table('quoter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'quoter', ['Quoter'])


    def backwards(self, orm):
        # Deleting model 'Quoter'
        db.delete_table('quoter')


    models = {
        u'quoter.quoter': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Quoter', 'db_table': "'quoter'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['quoter']