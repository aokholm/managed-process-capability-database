from django.conf.urls.defaults import patterns
from django.contrib import admin
from django.http import HttpResponse

from mesdata.models import Measurement, MeasurementSet
from mesdata.admin import MeasurementSetAdmin
from tags.models import *
from tags.admin import *

from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User

class MyAdminSite(admin.AdminSite):

    def get_urls(self):
        urls = super(MyAdminSite, self).get_urls()
        my_urls = patterns('',
            (r'^my_view2/$', self.admin_view(self.my_view)),
        )
        return my_urls + urls

    def my_view(self, request):
        return HttpResponse("Hello2")
        
admin_site = MyAdminSite('myadmin')  

admin_site.register(MeasurementSet,MeasurementSetAdmin)


admin_site.register(MaterialAlternativeName)
admin_site.register(Material, MaterialAdmin)
admin_site.register(ProcessAlternativeName)
admin_site.register(Process, ProcessAdmin)
admin_site.register(GeneralTag, GeneralTagAdmin)
admin_site.register(MeasurementEquipment, GeneralTagAdmin)


admin_site.register(Group, GroupAdmin)
admin_site.register(User, UserAdmin)



