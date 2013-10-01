from django.db import models
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