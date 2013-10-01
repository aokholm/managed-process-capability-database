from django.contrib import admin
from mesdata.models import Measurement, MeasurementSet


# admin MEASUREMENT
class MeasurementInline(admin.TabularInline):
    model = Measurement
    extra = 10

class MeasurementSetAdmin(admin.ModelAdmin):
    raw_id_fields = ('material',)
    inlines = [MeasurementInline]