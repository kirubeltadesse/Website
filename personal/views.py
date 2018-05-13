# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
	return render(request, 'personal/home.html')

def contact(request):
	return render(request, 'personal/basic.html', {'content':['if you want to contact me through', 'kiyamelak@gmail.com']})

def resume(request):
	return render(request, 'personal/resume.html')

# Create your views here.
