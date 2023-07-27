from django.urls import path
from . import views

urlpatterns = [
    #paths del services
    path('', views.services, name="services"),
 
]