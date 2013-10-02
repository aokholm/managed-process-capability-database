from django.http import Http404, HttpResponseRedirect, HttpResponse

# Create your views here.
def index(request):
        return HttpResponse("Hello2")