# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url   
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^contact/', views.contact, name='contact'),
	url(r'^resume/', views.resume, name='resume'),
	
]

# Create your views here.
