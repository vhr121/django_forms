# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def hello(request):
 return render(request,"app1/template/index.html")

def form(request):
 return render(request,"app1/template/form.html")
 

# Create your views here.
