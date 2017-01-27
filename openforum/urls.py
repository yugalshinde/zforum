"""
URL configuration for openforum
"""

from django.conf.urls import url
from . import views

# The URL patterns list routes URLs to views.
urlpatterns = [url(r'^$', views.index, name='index'),]