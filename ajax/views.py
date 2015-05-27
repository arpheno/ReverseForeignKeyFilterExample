from django.contrib.redirects.models import Redirect
from django.shortcuts import render

# Create your views here.
def myFunction(request):
    if request.method == 'POST':
        num_results = int(request.POST.get('num_results'))
        print "\n\POST: " + str(request.POST) + "\n\n"
        return Redirect("/")
    else:
        print "body:"+request.body
        num_results = int(request.GET['num_results'])
        print "\n\GET: " + str(request.GET) + "\n\n"
        return Redirect("/")