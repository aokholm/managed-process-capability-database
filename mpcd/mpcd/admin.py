from django.conf.urls.defaults import patterns
from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse

from mesdata.models import Measurement, MeasurementSet
from mesdata.admin import MeasurementSetAdmin
from tags.models import *
from tags.admin import *

from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User

class MyAdminSite(admin.AdminSite):

    index_template = 'admin/index_mod.html'

    def get_urls(self):
        urls = super(MyAdminSite, self).get_urls()

        my_urls = patterns('',
            # (r'^$', self.admin_view(self.index_mod), name='index_mod'),
            # (r'^analyze/$', self.admin_view(self.my_view)),
            url(r'^analyze/$', include('analyze.urls', namespace="analyze")),
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



