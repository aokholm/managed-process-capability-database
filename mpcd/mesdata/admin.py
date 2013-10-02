from django.contrib import admin
from mesdata.models import Measurement, MeasurementSet
from numpy import mean


# admin MEASUREMENT
class MeasurementInline(admin.TabularInline):
    model = Measurement
    extra = 10

class MeasurementSetAdmin(admin.ModelAdmin):
    raw_id_fields = ('material',)
    inlines = [MeasurementInline]

    def response_add(self, request, new_object):
        obj = self.after_saving_model_and_related_inlines(new_object)
        return super(MeasurementSetAdmin, self).response_add(request, obj)

    def response_change(self, request, obj):
        obj = self.after_saving_model_and_related_inlines(obj)
        return super(MeasurementSetAdmin, self).response_change(request, obj)

    def after_saving_model_and_related_inlines(self, obj):
        #print obj.related_set.all()
        measurements = [x.value for x in obj.measurements.all()]
        obj.measurement_count = len(measurements)
        obj.measurement_mean = mean(measurements)
        obj.save()
        return obj