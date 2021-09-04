from typing import Pattern
from django.conf.urls import url
from django.urls import path
from . import views

urlPattern = [
    path('', views.index , name='index')
]