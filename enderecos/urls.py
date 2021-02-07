from django.urls import path
# from django.contrib import admin
from . import views

app_name = 'enderecos'

urlpatterns = [
    path('', views.AddressFormView.as_view(), name='enderecos'),
    ]
