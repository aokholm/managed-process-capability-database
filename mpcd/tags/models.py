from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from string import join
from django.contrib import admin
from mptt.admin import MPTTModelAdmin


## Models
class MaterialAlternativeName(models.Model):
    name = models.CharField(max_length=60, unique=True)
    material_node = models.ForeignKey('Material', related_name='material_names')

    def __unicode__(self):
        return self.name

class ProcessAlternativeName(models.Model):
    name = models.CharField(max_length=60, unique=True)
    process_node = models.ForeignKey('Process', related_name='process_names')

    def __unicode__(self):
        return self.name


class Material(MPTTModel):
    name = models.CharField(max_length=60, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    
    def __unicode__(self):
        return self.name

    def alternative_names_(self):
        lst = [x.name for x in self.material_names.all()]
        return str(join(lst, ', '))

    class MPTTMeta:
        order_insertion_by = ['name']


class Process(MPTTModel):
    name = models.CharField(max_length=60, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    
    def __unicode__(self):
        return self.name

    def alternative_names_(self):
        lst = [x.name for x in self.process_names.all()]
        return str(join(lst, ', '))

    class MPTTMeta:
        order_insertion_by = ['name']


class GeneralTag(MPTTModel):
    name = models.CharField(max_length=60, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    
    def __unicode__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

class MeasurementEquipment(MPTTModel):
    name = models.CharField(max_length=60, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    
    def __unicode__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']