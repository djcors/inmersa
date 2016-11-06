# coding: utf-8
from django.conf import settings
from django.utils.crypto import get_random_string
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import *
from products_engine.models import Plato

@receiver(post_save, sender=Compra)
def post_save_compra(sender, instance, created=None, **kwargs):
    if created:
        unique_id = get_random_string(length=15)
        instance.identificador = unique_id
        instance.valor = instance.plato.valor
        instance.save()

@receiver(post_delete, sender=Compra)
def post_delete_compra(sender, instance, **kwargs):
    plato = Plato.objects.get(pk=instance.plato.pk)
    plato.stock += 1
    plato.comprados -= 1
    plato.save()
