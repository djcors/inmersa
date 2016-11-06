# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import *

class CompraAdmin(admin.ModelAdmin):
    list_display = ('identificador','usuario','valor','plato')

admin.site.register(Compra, CompraAdmin)
