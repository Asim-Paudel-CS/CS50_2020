from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def dateshome(request):
    curdate = datetime.datetime.now()
    y=curdate.year
    m=curdate.month
    d=curdate.day
    h=curdate.hour
    m=curdate.minute
    s=curdate.second
    boolvar = y == 1 and m == 1
    return render(request,"dateapp/datecheck.html",{"ye":y,"mo":m,"da":d,"ho":h,"mi":m,"se":s,"boolvariable":boolvar})