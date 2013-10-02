from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from mesdata.models import MeasurementSet

import numpy as np, math
# # import matplotlib.pyplot as plt
from prettytable import PrettyTable
from scipy.stats import norm, chi2
#from lib.ITGrade import ITGrade as itg

#import scipy.stats as ss


# Create your views here.
def index(request, app_name):
    app_dict = {
        'name': app_name,
    }

    return render(request, 'analyze/index.html', {'app_list': [app_dict],})


def process(request, app_name):
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


    return render(request, 'analyze/process.html', 
        {
            'app_label': app_name,
            'view_label': 'process',
            'itgrades' : itgrades,
            'measurement_sets': measurements_sets,
            'table' : mytable,

        })

def design(request, app_name):
    return render(request, 'analyze/process.html', 
        {
            'app_label': app_name,
            'view_label': 'design'
        })
        