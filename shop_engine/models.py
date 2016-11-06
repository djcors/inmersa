# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from products_engine.models import Plato

class Compra(models.Model):
    usuario = models.ForeignKey(User, related_name='apps_compras',
                                verbose_name=_(u'Usuario'))
    plato = models.ForeignKey(Plato, verbose_name=_(u"Plato"))
    identificador = models.CharField(_(u'Código de la compra'), blank=True, null=True, max_length=15)
    valor = models.PositiveIntegerField(_(u"Valor"), default=0)


    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

    def __str__(self):
        return self.plato.nombre
    


from .signals import *