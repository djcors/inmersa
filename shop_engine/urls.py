# -*- coding: utf-8 -*-
from django.conf import settings

from django.conf.urls import url, include, patterns
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('shop_engine.views',
    url(r'^comprar/$', 'comprar', name="comprar"),
)
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])