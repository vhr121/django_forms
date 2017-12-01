from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$',views.hello),
    url(r'formsubmit',views.form),
    
]
