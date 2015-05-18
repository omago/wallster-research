# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Quote'
        db.create_table('quote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quoter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quoter.Quoter'])),
            ('quote', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'quote', ['Quote'])

        # Adding M2M table for field quote_category on 'Quote'
        m2m_table_name = db.shorten_name('quote_quote_category')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('quote', models.ForeignKey(orm[u'quote.quote'], null=False)),
            ('quotecategory', models.ForeignKey(orm[u'quote_category.quotecategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['quote_id', 'quotecategory_id'])


    def backwards(self, orm):
        # Deleting model 'Quote'
        db.delete_table('quote')

        # Removing M2M table for field quote_category on 'Quote'
        db.delete_table(db.shorten_name('quote_quote_category'))


    models = {
        u'quote.quote': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Quote', 'db_table': "'quote'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quote': ('django.db.models.fields.TextField', [], {}),
            'quote_category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['quote_category.QuoteCategory']", 'symmetrical': 'False'}),
            'quoter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quoter.Quoter']"})
        },
        u'quote_category.quotecategory': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'QuoteCategory', 'db_table': "'quote_category'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'quoter.quoter': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Quoter', 'db_table': "'quoter'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['quote']