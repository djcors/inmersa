# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class Plato(models.Model):

    usuario = models.ForeignKey(User, related_name='apps_plato',
                                verbose_name=_(u'Usuario'))
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(_(u"Nombre"), max_length=200)
    descripcion = models.TextField(_(u"Descripción"), blank=True, null=True)
    ingredientes = models.TextField(_(u"Ingredientes"), blank=True, null=True)
    activo = models.BooleanField(_(u'Activo'), default=True)
    valor = models.PositiveIntegerField(_(u"Valor"),default=0)
    calorias = models.CharField(_(u"Calorias"), max_length=200, blank=True, null=True)
    grasa = models.CharField(_(u"Grasa"), max_length=200, blank=True, null=True)
    zona = models.CharField(_(u"Zona"), max_length=200, null=True, blank=True)
    foto = models.ImageField(_(u'Foto'), upload_to='uploads/platos/imagenes/')
    fav = models.ManyToManyField(User, _(u"Favorito"), null=True, blank=True)
    shared = models.PositiveIntegerField(_(u"Compartidos"), default=0)
    comprados = models.PositiveIntegerField(_(u"Compras"), default=0)
    stock = models.PositiveIntegerField(_(u"Stock"), default=0)

    class Meta:
        verbose_name = "Plato"
        verbose_name_plural = "Platos"

    def __str__(self):
        return "%s (%s)" % (self.nombre, self.codigo)

    def __unicode__(self):
        return self.nombre

    @property
    def activa(self):
        return self.activo

