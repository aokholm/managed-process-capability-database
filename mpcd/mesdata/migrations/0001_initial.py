# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MeasurementSet'
        db.create_table(u'mesdata_measurementset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('measurementCount', self.gf('django.db.models.fields.IntegerField')()),
            ('material', self.gf('django.db.models.fields.related.ForeignKey')(related_name='measurement_sets', to=orm['tags.Material'])),
        ))
        db.send_create_signal(u'mesdata', ['MeasurementSet'])


    def backwards(self, orm):
        # Deleting model 'MeasurementSet'
        db.delete_table(u'mesdata_measurementset')


    models = {
        u'mesdata.measurementset': {
            'Meta': {'object_name': 'MeasurementSet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'measurement_sets'", 'to': u"orm['tags.Material']"}),
            'measurementCount': ('django.db.models.fields.IntegerField', [], {})
        },
        u'tags.material': {
            'Meta': {'object_name': 'Material'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['tags.Material']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['mesdata']