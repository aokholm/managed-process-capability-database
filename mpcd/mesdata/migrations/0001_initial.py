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
            ('actual_size', self.gf('django.db.models.fields.FloatField')()),
            ('measurement_set', self.gf('django.db.models.fields.related.ForeignKey')(related_name='measurements', to=orm['mesdata.MeasurementSet'])),
        ))
        db.send_create_signal(u'mesdata', ['Measurement'])

        # Adding model 'MeasurementSet'
        db.create_table(u'mesdata_measurementset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('measurement_count', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('measurement_mean', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('measurement_std', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('measurement_itg', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('nominal_size', self.gf('django.db.models.fields.FloatField')()),
            ('tol_up', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('tol_low', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('manufac', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('measured', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('machine', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('pro_yield', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('material', self.gf('django.db.models.fields.related.ForeignKey')(related_name='measurement_sets', to=orm['tags.Material'])),
            ('process', self.gf('django.db.models.fields.related.ForeignKey')(related_name='measurement_sets', to=orm['tags.Process'])),
            ('equipment', self.gf('django.db.models.fields.related.ForeignKey')(related_name='measurement_sets', to=orm['tags.MeasurementEquipment'])),
            ('measurement_type', self.gf('django.db.models.fields.CharField')(default='L', max_length=1)),
        ))
        db.send_create_signal(u'mesdata', ['MeasurementSet'])

        # Adding M2M table for field generaltag on 'MeasurementSet'
        m2m_table_name = db.shorten_name(u'mesdata_measurementset_generaltag')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('measurementset', models.ForeignKey(orm[u'mesdata.measurementset'], null=False)),
            ('generaltag', models.ForeignKey(orm[u'tags.generaltag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['measurementset_id', 'generaltag_id'])


    def backwards(self, orm):
        # Deleting model 'Measurement'
        db.delete_table(u'mesdata_measurement')

        # Deleting model 'MeasurementSet'
        db.delete_table(u'mesdata_measurementset')

        # Removing M2M table for field generaltag on 'MeasurementSet'
        db.delete_table(db.shorten_name(u'mesdata_measurementset_generaltag'))


    models = {
        u'mesdata.measurement': {
            'Meta': {'object_name': 'Measurement'},
            'actual_size': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'measurement_set': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'measurements'", 'to': u"orm['mesdata.MeasurementSet']"})
        },
        u'mesdata.measurementset': {
            'Meta': {'object_name': 'MeasurementSet'},
            'equipment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'measurement_sets'", 'to': u"orm['tags.MeasurementEquipment']"}),
            'generaltag': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'measurement_sets'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['tags.GeneralTag']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'manufac': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'measurement_sets'", 'to': u"orm['tags.Material']"}),
            'measured': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'measurement_count': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'measurement_itg': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'measurement_mean': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'measurement_std': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'measurement_type': ('django.db.models.fields.CharField', [], {'default': "'L'", 'max_length': '1'}),
            'nominal_size': ('django.db.models.fields.FloatField', [], {}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pro_yield': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'process': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'measurement_sets'", 'to': u"orm['tags.Process']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'tol_low': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tol_up': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
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