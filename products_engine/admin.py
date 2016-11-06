# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from .models import *


class ImagenAdminForm(forms.ModelForm):
    def clean_imagen(self):
        imagen = self.cleaned_data['imagen']
        if not imagen:
            raise ValidationError(_(u'El campo imagen es obligatorio'))
        else:
            try:
                imagen.name.encode("ascii")
            except UnicodeEncodeError:
                raise ValidationError(_(u'Nombre de archivo incorrecto'))
        return self.cleaned_data["imagen"]



class PlatoAdmin(admin.ModelAdmin):
    list_display = ('usuario','codigo', 'valor', 'activo','stock', )
    list_filter = ('usuario',)
    list_editable = ('stock',)
    filter_horizontal = ('fav',)
    fieldsets = [
        [_(u'Informativo'), {
            'fields': (
                'usuario', 'codigo','foto','valor',
                'stock','activo','fav'
            )
        }],
        [_(u'General'), {
            'fields': (
                'nombre', 'descripcion','zona','ingredientes',
                'calorias','grasa',
            )
        }],
    ]
admin.site.register(Plato, PlatoAdmin)
