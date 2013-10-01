from django.db import models
from django.contrib import admin
from numpy import mean

# Create your models here.
class Measurement(models.Model):
    value = models.FloatField()
    measurement_set = models.ForeignKey('MeasurementSet', related_name='measurements')

    def __unicode__(self):
        return str(self.value)


class MeasurementSet(models.Model):
    measurement_count = models.IntegerField(blank=True)
    measurement_mean = models.FloatField(blank=True)
    material = models.ForeignKey('tags.Material', related_name='measurement_sets')

    def __unicode__(self):
        return """material: %s, samples %s, """ % (self.material.name, self.measurement_count)

    def save(self, *args, **kwargs):
        measurements = [x.value for x in self.measurements.all()]
        self.measurement_count = len(measurements)
        self.measurement_mean = mean(measurements)
        super(MeasurementSet, self).save(*args, **kwargs)


# admin
class MeasurementInline(admin.TabularInline):
    model = Measurement
    extra = 10

# class MeasurementAdmin(admin.ModelAdmin):
#     fields = 
        

class MeasurementSetAdmin(admin.ModelAdmin):
    raw_id_fields = ('material',)
    inlines = [MeasurementInline]

admin.site.register(MeasurementSet,MeasurementSetAdmin)