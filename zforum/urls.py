"""
forum URL Configuration
"""

from django.conf.urls import url, include
from django.contrib import admin
admin.autodiscover()
#from rest_framework import routers, serializers, viewsets
#from openforum.models import Question, User, Answer, Comment, Configuration
from openforum.router import router

router_class = router()
returned_router = router_class.set_router()

# Url pattern list routes URLs to views.
urlpatterns = [
    url(r'^openforum/', include('openforum.urls')),
    url(r'^admin', include(admin.site.urls)),
    url(r'^', include(returned_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]