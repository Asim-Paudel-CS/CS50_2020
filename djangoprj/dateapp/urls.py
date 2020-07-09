from . import views
from django.urls import path

urlpatterns = [
    path("",views.dateshome,name="dateshome")
]