from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
<<<<<<< HEAD
from mesdata.models import MeasurementSet, Queries
=======
from mesdata.models import MeasurementSet
>>>>>>> parent of e91d61a... Created chart helper function. Updated design plus view to use chart helper

import numpy as np, math
# # import matplotlib.pyplot as plt
from prettytable import PrettyTable
from scipy.stats import norm, chi2
#from lib.ITGrade import ITGrade as itg

#import scipy.stats as ss

<<<<<<< HEAD
import gviz_api
from django.utils.safestring import mark_safe
=======
>>>>>>> parent of e91d61a... Created chart helper function. Updated design plus view to use chart helper

# Create your views here.
def index(request, app_name):
    app_dict = {
        'name': app_name,
    }

    return render(request, 'analyze/index.html', {'app_list': [app_dict],})


def design(request, app_name):
    measurements_sets = MeasurementSet.objects.all().prefetch_related('process', 'material')

    itgrades = sorted([messet.measurement_itg for messet in measurements_sets])
    input_data = itgrades
    Ndata = len(input_data)
    number = [i for i in range(1,Ndata+1)]
    cum_rank =[i*(1/float(Ndata+1)) for i in range(1, Ndata+1)]
    mean = np.mean(input_data)
    std = np.std(input_data, ddof=1)

    cum_frequency = [norm.cdf(input_data[i], loc=mean, scale=std) for i in range(Ndata)]
    cum_std = [math.sqrt(cum_frequency[i]*(1-cum_frequency[i]) / Ndata)  for i in range(Ndata)]

    t = 1.71 # for N > 10

    ll = [cum_frequency[i] - 2*cum_frequency[i] * t * cum_std[i] for i in range(Ndata)]
    ul = [cum_frequency[i] + 2*(1-cum_frequency[i]) * t * cum_std[i] for i in range(Ndata)]

    mytable = PrettyTable()

    mytable.add_column("Sortet input data", input_data)
    mytable.add_column("#number", number)
    mytable.add_column("cum_rank", cum_rank)
    mytable.add_column("cum_frequency", cum_frequency)
    mytable.add_column("cum_std", cum_std)
    mytable.add_column("lower limit", ll)
    mytable.add_column("upper limit", ul)

    # find plot range 
    plotStart   = norm.isf(0.001, loc=mean, scale=std)
    plotEnd     = norm.isf(0.999, loc=mean, scale=std)

    x = np.linspace(plotStart,plotEnd, 100)
    cdf = [norm.cdf(x[i], loc=mean, scale=std) for i in range(100)]
    cdf_std = [math.sqrt(cdf[i]*(1-cdf[i]) / Ndata)  for i in range(100)]
    cdfll = [cdf[i] - 2*cdf[i] * t * cdf_std[i] for i in range(100)]
    cfdul = [cdf[i] + 2*(1-cdf[i]) * t * cdf_std[i] for i in range(100)]


    return render(request, 'analyze/design.html', 
        {
            'app_label': app_name,
            'view_label': 'design',
            'itgrades' : itgrades,
            'measurement_sets': measurements_sets,
            'table' : mytable,

        })
<<<<<<< HEAD

def process(request, app_name):
    measurements_sets = MeasurementSet.objects.all()

    bias = [messet.measurement_bias for messet in measurements_sets]
    dev = [messet.measurement_std for messet in measurements_sets]

    # Creating the data
    description = [("Bias", "number"), ("Deviation", "number")]
    data = zip(bias,dev)

    #zip(bias,dev) 

    # Loading it into gviz_api.DataTable
    data_table = gviz_api.DataTable(description)
    data_table.LoadData(data)

    # Creating a JSon string
    json = data_table.ToJSon()

    questions=None
    if request.GET.get('search'):
        search = request.GET.get('search')
        questions = Queries.objects.filter(query__icontains=search)

        name = request.GET.get('name')
        query = Queries.objects.create(query=search, user_id=name)
        query.save()


=======
>>>>>>> parent of e91d61a... Created chart helper function. Updated design plus view to use chart helper

    return render(request, 'analyze/process.html', 
        {
            'app_label': app_name,
<<<<<<< HEAD
            'view_label': 'process',
            'measurement_sets': measurements_sets,
            'json' : mark_safe(json),
            'questions': questions,
        })
=======
            'view_label': 'process'
        })
        
>>>>>>> parent of e91d61a... Created chart helper function. Updated design plus view to use chart helper
