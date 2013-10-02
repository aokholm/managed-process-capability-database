from django.contrib import admin
from mesdata.models import Measurement, MeasurementSet, Mestype
from mesdata.ITGrade import stdbias2itg
from numpy import mean, std


# admin MEASUREMENT
class MeasurementInline(admin.TabularInline):
    model = Measurement
    extra = 10

class MestypeAdmin(admin.TabularInline):
    model = Mestype
    extra = 1

class MeasurementSetAdmin(admin.ModelAdmin):
    raw_id_fields = ('material','process','generaltag','equipment')
    autocomplete_lookup_fields = {
        'fk':['material','process']
    }
    
    readonly_fields = ('id',)

    fieldsets = [
    (None,                          {'fields': ['nominal_size','material','process','generaltag','equipment','tol_up','tol_low','pub_date' ]}),
    ('Confidential information',    {'fields': ['price','weight','manufac','measured','machine','pro_yield']}),
    ]

    inlines = [MeasurementInline, MestypeAdmin]

    list_display = ('id','measurement_count','measurement_itg','nominal_size','pub_date',)

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
        nominal_size = obj.nominal_size

        obj.measurement_cpk = 1.33
        obj.measurement_bias = nominal_size - mean(measurements)
        obj.measurement_std = std(measurements)
        obj.measurement_itg = stdbias2itg(nominal_size, obj.measurement_std, obj.measurement_bias, obj.measurement_cpk,)
        obj.save()
        return obj