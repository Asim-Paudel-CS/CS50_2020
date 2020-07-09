from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Homepage!")

def hello(request):
    return HttpResponse("Hello, world!")

#def name(request,nam):
#   return HttpResponse(f"Hello, {nam.capitalize()}!")

def renderhtml(request,nam):
    return render(request,"djangoapp/render.html",{"name":nam.capitalize()})