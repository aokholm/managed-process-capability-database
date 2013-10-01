# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Measurement'
        db.create_table(u'mesdata_measurement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
            ('measurement_set', self.gf('django.db.models.fields.related.ForeignKey')(related_name='measurements', to=orm['mesdata.MeasurementSet'])),
        ))
        db.send_create_signal(u'mesdata', ['Measurement'])

        # Deleting field 'MeasurementSet.measurementCount'
        db.delete_column(u'mesdata_measurementset', 'measurementCount')

        # Adding field 'MeasurementSet.measurement_count'
        db.add_column(u'mesdata_measurementset', 'measurement_count',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'MeasurementSet.measurement_mean'
        db.add_column(u'mesdata_measurementset', 'measurement_mean',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Measurement'
        db.delete_table(u'mesdata_measurement')


        # User chose to not deal with backwards NULL issues for 'MeasurementSet.measurementCount'
        raise RuntimeError("Cannot reverse this migration. 'MeasurementSet.measurementCount' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'MeasurementSet.measurementCount'
        db.add_column(u'mesdata_measurementset', 'measurementCount',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)

        # Deleting field 'MeasurementSet.measurement_count'
        db.delete_column(u'mesdata_measurementset', 'measurement_count')

        # Deleting field 'MeasurementSet.measurement_mean'
        db.delete_column(u'mesdata_measurementset', 'measurement_mean')


    models = {
        u'mesdata.measurement': {
            'Meta': {'object_name': 'Measurement'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'measurement_set': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'measurements'", 'to': u"orm['mesdata.MeasurementSet']"}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        u'mesdata.measurementset': {
            'Meta': {'object_name': 'MeasurementSet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'measurement_sets'", 'to': u"orm['tags.Material']"}),
            'measurement_count': ('django.db.models.fields.IntegerField', [], {}),
            'measurement_mean': ('django.db.models.fields.FloatField', [], {})
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