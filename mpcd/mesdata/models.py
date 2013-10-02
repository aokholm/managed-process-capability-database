from django.db import models


# Create your models here.
class Measurement(models.Model):
    value = models.FloatField()
    measurement_set = models.ForeignKey('MeasurementSet', related_name='measurements')

    def __unicode__(self):
        return str(self.value)


class MeasurementSet(models.Model):
    measurement_count = models.IntegerField(blank=True, default=0)
    measurement_mean = models.FloatField(blank=True, null=True)
    material = models.ForeignKey('tags.Material', related_name='measurement_sets')

    def __unicode__(self):
        return """material: %s, samples %s, """ % (self.material.name, self.measurement_count)
        