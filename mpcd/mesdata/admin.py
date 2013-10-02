from django.contrib import admin
from mesdata.models import Measurement, MeasurementSet, Mestype
from numpy import mean, std


# admin MEASUREMENT
class MeasurementInline(admin.TabularInline):
    model = Measurement
    extra = 10

class MestypeAdmin(admin.TabularInline):
    model = Mestype
    extra = 1

class MeasurementSetAdmin(admin.ModelAdmin):
    raw_id_fields = ('material',)

    fieldsets = [
    (None,                          {'fields': ['nominal_size','material','tol_up','tol_low','pub_date' ]}),
    ('Confidential information',    {'fields': ['price','weight','manufac','measured','machine','pro_yield']}),
    ]

    inlines = [MeasurementInline, MestypeAdmin]

    list_display = ('measurement_count','measurement_std','nominal_size','pub_date',)

    def response_add(self, request, new_object):
        obj = self.after_saving_model_and_related_inlines(new_object)
        return super(MeasurementSetAdmin, self).response_add(request, obj)

    def response_change(self, request, obj):
        obj = self.after_saving_model_and_related_inlines(obj)
        return super(MeasurementSetAdmin, self).response_change(request, obj)

    def after_saving_model_and_related_inlines(self, obj):
        #print obj.related_set.all()
        measurements = [x.actual_size for x in obj.measurements.all()]
        obj.measurement_count = len(measurements)
        obj.measurement_mean = mean(measurements)
        obj.measurement_std = std(measurements)
        obj.save()
        return obj