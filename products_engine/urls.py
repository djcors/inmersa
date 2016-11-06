# -*- coding: utf-8 -*-
from django.conf import settings

from django.conf.urls import url, include, patterns
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('products_engine.views',
    url(r'^platos/$', 'Platos', name="api_platos"),
    url(r'^fav/$', 'fav_button', name="like"),
)
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])