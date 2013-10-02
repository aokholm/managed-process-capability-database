from django.db import models


# Create your models here.
class Measurement(models.Model):
    """ The Measured data for a simple component """
    actual_size = models.FloatField('Actual size') 
    recoded_date = models.DateField('Recoded date',blank=True, null=True)

    measurement_set = models.ForeignKey('MeasurementSet', related_name='measurements')


    def __unicode__(self):
        return str(self.actual_size)

class Mestype(models.Model):
    """ Choose type of Measurement"""
    measurement_set = models.ForeignKey('MeasurementSet')
    ANGLE = 'A'
    LENGTH = 'L'
    CIRCULARITY = 'C'
    PARALLELLITY = 'P'
    MESTYPE_CHOICES = (
        (ANGLE, 'Angle'),
        (LENGTH, 'length'),
        (CIRCULARITY, 'Circularity'),
        (PARALLELLITY, 'parallellity'),
    )
    mestype = models.CharField(max_length=1, choices=MESTYPE_CHOICES, default='L')

    def __unicode__(self):
        return self.mestype

class MeasurementSet(models.Model):
    measurement_count = models.IntegerField('No. Measurements',blank=True, default=0)
    measurement_mean = models.FloatField(blank=True, null=True)
    measurement_std = models.FloatField('Standard deviation',blank=True, null=True)

    nominal_size = models.FloatField('Nominal Size')
    tol_up = models.FloatField('Upper tolerance',blank=True, null=True) 
    tol_low = models.FloatField('Lower tolerance',blank=True, null=True)  
    price = models.FloatField('Price',blank=True, null=True) 
    weight = models.FloatField('Weight',blank=True, null=True)
    manufac = models.CharField(max_length=200,blank=True, null=True)
    measured = models.CharField(max_length=200,blank=True, null=True)
    machine = models.CharField(max_length=200,blank=True, null=True)
    pro_yield = models.CharField(max_length=200,blank=True, null=True)
    pub_date = models.DateTimeField('date published')

    material = models.ForeignKey('tags.Material', related_name='measurement_sets')

    def __unicode__(self):
        return """No.samples %s, Material: %s, Size: %s""" % (self.material.name, self.measurement_count,self.nominal_size)
    






