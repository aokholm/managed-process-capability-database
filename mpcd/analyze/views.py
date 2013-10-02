from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request, app_name):
    app_dict = {
        'name': app_name,
    }

    return render(request, 'analyze/index.html', {'app_list': [app_dict],})


def process(request, app_name):
    return render(request, 'analyze/process.html', 
        {
            'app_label': app_name,
            'view_label': 'process'
        })

def design(request, app_name):
    return render(request, 'analyze/process.html', 
        {
            'app_label': app_name,
            'view_label': 'design'
        })
        