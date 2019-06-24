from django.contrib import admin
from django.urls import path
from . import views
app_name='mongo'
urlpatterns = [
    path('fpage', views.home , name='fpage'),
]
