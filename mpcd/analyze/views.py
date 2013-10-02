from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    app_dict = {
        'name': 'analyze', # app_label.title()
        'app_url': 'analyze',
    }

    return render(request, 'analyze/index2.html', {'app_list': [app_dict],})
        