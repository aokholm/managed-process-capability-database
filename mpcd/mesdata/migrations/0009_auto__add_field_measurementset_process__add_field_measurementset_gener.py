# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MeasurementSet.process'
        db.add_column(u'mesdata_measurementset', 'process',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, related_name='measurement_sets', to=orm['tags.Process']),
                      keep_default=False)

        # Adding field 'MeasurementSet.generaltag'
        db.add_column(u'mesdata_measurementset', 'generaltag',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, related_name='measurement_sets', to=orm['tags.GeneralTag']),
                      keep_default=False)

        # Adding field 'MeasurementSet.equipment'
        db.add_column(u'mesdata_measurementset', 'equipment',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, related_name='measurement_sets', to=orm['tags.MeasurementEquipment']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MeasurementSet.process'
        db.delete_column(u'mesdata_measurementset', 'process_id')

        # Deleting field 'MeasurementSet.generaltag'
        db.delete_column(u'mesdata_measurementset', 'generaltag_id')

        # Deleting field 'MeasurementSet.equipment'
        db.delete_column(u'mesdata_measurementset', 'equipment_id')


    models = {
        u'mesdata.measurement': {
            'Meta': {'object_name': 'Measurement'},
            'actual_size': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'measurement_set': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'measurements'", 'to': u"orm['mesdata.MeasurementSet']"}),
            'recoded_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'mesdata.measurementset': {
            'Meta': {'object_name': 'MeasurementSet'},
            'equipment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'measurement_sets'", 'to': u"orm['tags.MeasurementEquipment']"}),
            'generaltag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'measurement_sets'", 'to': u"orm['tags.GeneralTag']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'manufac': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'measurement_sets'", 'to': u"orm['tags.Material']"}),
            'measured': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'measurement_ITG': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'measurement_count': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'measurement_mean': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'measurement_std': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'nominal_size': ('django.db.models.fields.FloatField', [], {}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pro_yield': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'process': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'measurement_sets'", 'to': u"orm['tags.Process']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'tol_low': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tol_up': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'mesdata.mestype': {
            'Meta': {'object_name': 'Mestype'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'measurement_set': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mesdata.MeasurementSet']"}),
            'mestype': ('django.db.models.fields.CharField', [], {'default': "'L'", 'max_length': '1'})
        },
        u'tags.generaltag': {
            'Meta': {'object_name': 'GeneralTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['tags.GeneralTag']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
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
        },
        u'tags.measurementequipment': {
            'Meta': {'object_name': 'MeasurementEquipment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['tags.MeasurementEquipment']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'tags.process': {
            'Meta': {'object_name': 'Process'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['tags.Process']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['mesdata']