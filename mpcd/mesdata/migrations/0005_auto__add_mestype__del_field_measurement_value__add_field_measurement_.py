# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Mestype'
        db.create_table(u'mesdata_mestype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('measurement_set', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mesdata.MeasurementSet'])),
            ('mestype', self.gf('django.db.models.fields.CharField')(default='L', max_length=1)),
        ))
        db.send_create_signal(u'mesdata', ['Mestype'])

        # Deleting field 'Measurement.value'
        db.delete_column(u'mesdata_measurement', 'value')

        # Adding field 'Measurement.actual_size'
        db.add_column(u'mesdata_measurement', 'actual_size',
                      self.gf('django.db.models.fields.FloatField')(default=2),
                      keep_default=False)

        # Adding field 'Measurement.recoded_date'
        db.add_column(u'mesdata_measurement', 'recoded_date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 10, 2, 0, 0)),
                      keep_default=False)

        # Adding field 'MeasurementSet.nominal_size'
        db.add_column(u'mesdata_measurementset', 'nominal_size',
                      self.gf('django.db.models.fields.FloatField')(default=100),
                      keep_default=False)

        # Adding field 'MeasurementSet.tol_up'
        db.add_column(u'mesdata_measurementset', 'tol_up',
                      self.gf('django.db.models.fields.FloatField')(default=1),
                      keep_default=False)

        # Adding field 'MeasurementSet.tol_low'
        db.add_column(u'mesdata_measurementset', 'tol_low',
                      self.gf('django.db.models.fields.FloatField')(default=-1),
                      keep_default=False)

        # Adding field 'MeasurementSet.price'
        db.add_column(u'mesdata_measurementset', 'price',
                      self.gf('django.db.models.fields.FloatField')(default=1000),
                      keep_default=False)

        # Adding field 'MeasurementSet.weight'
        db.add_column(u'mesdata_measurementset', 'weight',
                      self.gf('django.db.models.fields.FloatField')(default=10),
                      keep_default=False)

        # Adding field 'MeasurementSet.manufac'
        db.add_column(u'mesdata_measurementset', 'manufac',
                      self.gf('django.db.models.fields.CharField')(default=23, max_length=200),
                      keep_default=False)

        # Adding field 'MeasurementSet.measured'
        db.add_column(u'mesdata_measurementset', 'measured',
                      self.gf('django.db.models.fields.CharField')(default=34, max_length=200),
                      keep_default=False)

        # Adding field 'MeasurementSet.machine'
        db.add_column(u'mesdata_measurementset', 'machine',
                      self.gf('django.db.models.fields.CharField')(default=200, max_length=200),
                      keep_default=False)

        # Adding field 'MeasurementSet.pro_yield'
        db.add_column(u'mesdata_measurementset', 'pro_yield',
                      self.gf('django.db.models.fields.CharField')(default=203, max_length=200),
                      keep_default=False)

        # Adding field 'MeasurementSet.pub_date'
        db.add_column(u'mesdata_measurementset', 'pub_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 2, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Mestype'
        db.delete_table(u'mesdata_mestype')

        # Adding field 'Measurement.value'
        db.add_column(u'mesdata_measurement', 'value',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Deleting field 'Measurement.actual_size'
        db.delete_column(u'mesdata_measurement', 'actual_size')

        # Deleting field 'Measurement.recoded_date'
        db.delete_column(u'mesdata_measurement', 'recoded_date')

        # Deleting field 'MeasurementSet.nominal_size'
        db.delete_column(u'mesdata_measurementset', 'nominal_size')

        # Deleting field 'MeasurementSet.tol_up'
        db.delete_column(u'mesdata_measurementset', 'tol_up')

        # Deleting field 'MeasurementSet.tol_low'
        db.delete_column(u'mesdata_measurementset', 'tol_low')

        # Deleting field 'MeasurementSet.price'
        db.delete_column(u'mesdata_measurementset', 'price')

        # Deleting field 'MeasurementSet.weight'
        db.delete_column(u'mesdata_measurementset', 'weight')

        # Deleting field 'MeasurementSet.manufac'
        db.delete_column(u'mesdata_measurementset', 'manufac')

        # Deleting field 'MeasurementSet.measured'
        db.delete_column(u'mesdata_measurementset', 'measured')

        # Deleting field 'MeasurementSet.machine'
        db.delete_column(u'mesdata_measurementset', 'machine')

        # Deleting field 'MeasurementSet.pro_yield'
        db.delete_column(u'mesdata_measurementset', 'pro_yield')

        # Deleting field 'MeasurementSet.pub_date'
        db.delete_column(u'mesdata_measurementset', 'pub_date')


    models = {
        u'mesdata.measurement': {
            'Meta': {'object_name': 'Measurement'},
            'actual_size': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'measurement_set': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'measurements'", 'to': u"orm['mesdata.MeasurementSet']"}),
            'recoded_date': ('django.db.models.fields.DateField', [], {})
        },
        u'mesdata.measurementset': {
            'Meta': {'object_name': 'MeasurementSet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'manufac': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'measurement_sets'", 'to': u"orm['tags.Material']"}),
            'measured': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'measurement_count': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'measurement_mean': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'nominal_size': ('django.db.models.fields.FloatField', [], {}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'pro_yield': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'tol_low': ('django.db.models.fields.FloatField', [], {}),
            'tol_up': ('django.db.models.fields.FloatField', [], {}),
            'weight': ('django.db.models.fields.FloatField', [], {})
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