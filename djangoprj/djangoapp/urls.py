from django.urls import path
from . import views

urlpatterns= [
    path("",views.home,name="Homepage"),
    path("hello",views.hello,name="HW"),
    #path("<str:nam>",views.name,name="Helloname"),
    path("<str:nam>",views.renderhtml,name="Hi Name")    
]