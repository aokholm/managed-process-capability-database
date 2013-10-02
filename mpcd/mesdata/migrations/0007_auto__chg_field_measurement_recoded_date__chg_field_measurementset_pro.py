# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Measurement.recoded_date'
        db.alter_column(u'mesdata_measurement', 'recoded_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'MeasurementSet.pro_yield'
        db.alter_column(u'mesdata_measurementset', 'pro_yield', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'MeasurementSet.weight'
        db.alter_column(u'mesdata_measurementset', 'weight', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'MeasurementSet.price'
        db.alter_column(u'mesdata_measurementset', 'price', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'MeasurementSet.measured'
        db.alter_column(u'mesdata_measurementset', 'measured', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'MeasurementSet.manufac'
        db.alter_column(u'mesdata_measurementset', 'manufac', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'MeasurementSet.machine'
        db.alter_column(u'mesdata_measurementset', 'machine', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'MeasurementSet.tol_low'
        db.alter_column(u'mesdata_measurementset', 'tol_low', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'MeasurementSet.tol_up'
        db.alter_column(u'mesdata_measurementset', 'tol_up', self.gf('django.db.models.fields.FloatField')(null=True))

    def backwards(self, orm):

        # Changing field 'Measurement.recoded_date'
        db.alter_column(u'mesdata_measurement', 'recoded_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 10, 2, 0, 0)))

        # Changing field 'MeasurementSet.pro_yield'
        db.alter_column(u'mesdata_measurementset', 'pro_yield', self.gf('django.db.models.fields.CharField')(default=1, max_length=200))

        # Changing field 'MeasurementSet.weight'
        db.alter_column(u'mesdata_measurementset', 'weight', self.gf('django.db.models.fields.FloatField')(default=10))

        # Changing field 'MeasurementSet.price'
        db.alter_column(u'mesdata_measurementset', 'price', self.gf('django.db.models.fields.FloatField')(default=10))

        # Changing field 'MeasurementSet.measured'
        db.alter_column(u'mesdata_measurementset', 'measured', self.gf('django.db.models.fields.CharField')(default=10, max_length=200))

        # Changing field 'MeasurementSet.manufac'
        db.alter_column(u'mesdata_measurementset', 'manufac', self.gf('django.db.models.fields.CharField')(default=10, max_length=200))

        # Changing field 'MeasurementSet.machine'
        db.alter_column(u'mesdata_measurementset', 'machine', self.gf('django.db.models.fields.CharField')(default=10, max_length=200))

        # Changing field 'MeasurementSet.tol_low'
        db.alter_column(u'mesdata_measurementset', 'tol_low', self.gf('django.db.models.fields.FloatField')(default=2))

        # Changing field 'MeasurementSet.tol_up'
        db.alter_column(u'mesdata_measurementset', 'tol_up', self.gf('django.db.models.fields.FloatField')(default=2))

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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'manufac': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'measurement_sets'", 'to': u"orm['tags.Material']"}),
            'measured': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'measurement_count': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'measurement_mean': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'measurement_std': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'nominal_size': ('django.db.models.fields.FloatField', [], {}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pro_yield': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
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