from django.urls import path
from . import views

app_name= "tasksapp"
urlpatterns = [
    path("", views.homepagetask, name="homepagetask"),
    path("add", views.add, name="add"),
]