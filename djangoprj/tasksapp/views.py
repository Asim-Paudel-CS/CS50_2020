from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse

class Newform(forms.Form):
    task = forms.CharField(label="NewTask")
    #priority = forms.IntegerField(label="Priority", min_value=1,max_value=10)

tasks = ["hey", "hi", "hello"]
# Create your views here.
def homepagetask(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasksapp/taskapptemplate.html", {"tasksvar":request.session["tasks"]})

def add(request):
    if request.method == "POST":
        filledform = Newform(request.POST)
        if filledform.is_valid():
            task = filledform.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasksapp:homepagetask"))
        else:
            return render(request,"tasksapp/add.html",{"newformvar":filledform})

    return render(request, "tasksapp/add.html", {"newformvar":Newform()})
