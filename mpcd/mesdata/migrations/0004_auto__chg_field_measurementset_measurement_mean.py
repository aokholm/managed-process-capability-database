# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'MeasurementSet.measurement_mean'
        db.alter_column(u'mesdata_measurementset', 'measurement_mean', self.gf('django.db.models.fields.FloatField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'MeasurementSet.measurement_mean'
        raise RuntimeError("Cannot reverse this migration. 'MeasurementSet.measurement_mean' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'MeasurementSet.measurement_mean'
        db.alter_column(u'mesdata_measurementset', 'measurement_mean', self.gf('django.db.models.fields.FloatField')())

    models = {
        u'mesdata.measurement': {
            'Meta': {'object_name': 'Measurement'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'measurement_set': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'measurements'", 'to': u"orm['mesdata.MeasurementSet']"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        u'mesdata.measurementset': {
            'Meta': {'object_name': 'MeasurementSet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'measurement_sets'", 'to': u"orm['tags.Material']"}),
            'measurement_count': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'measurement_mean': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
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