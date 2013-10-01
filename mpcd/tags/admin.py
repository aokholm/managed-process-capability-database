from mptt.admin import MPTTModelAdmin
#from tags.models import 

## admin TAGS
class MaterialAdmin(MPTTModelAdmin):
    list_display = ['name', 'alternative_names_',]
    search_fields = ['name', 'material_names__name',]

    def queryset(self, request):
        return super(MaterialAdmin, self).queryset(request).prefetch_related('material_names')

class ProcessAdmin(MPTTModelAdmin):
    list_display = ['name', 'alternative_names_',]
    search_fields = ['name', 'process_names__name',]

    def queryset(self, request):
        return super(ProcessAdmin, self).queryset(request).prefetch_related('process_names')

class GeneralTagAdmin(MPTTModelAdmin):
    list_display = ['name',]
    search_fields = ['name',]

class MeasurementEquipmentAdmin(MPTTModelAdmin):
    list_display = ['name',]
    search_fields = ['name',]