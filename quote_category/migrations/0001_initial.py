# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'QuoteCategory'
        db.create_table('quote_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'quote_category', ['QuoteCategory'])


    def backwards(self, orm):
        # Deleting model 'QuoteCategory'
        db.delete_table('quote_category')


    models = {
        u'quote_category.quotecategory': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'QuoteCategory', 'db_table': "'quote_category'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['quote_category']