# -*- coding: utf-8 -*-
import json
import django_filters
import requests
from django.shortcuts import render
from django.http import HttpResponseNotAllowed, HttpResponseNotFound, HttpResponse, HttpResponseForbidden, HttpResponseRedirect, Http404, JsonResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import generics
from rest_framework import permissions
from django.core import serializers
from products_engine.models import Plato
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import *

@csrf_exempt
def comprar(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            codigos = request.POST['datos'].split(',')
            platos = Plato.objects.filter(codigo__in=codigos)
            for plato in platos:
                if plato.stock:
                    compra = Compra.objects.create(
                        plato=plato,
                        usuario=request.user,
                        valor=plato.valor
                    )
                    compra.save()
                    plato.stock -=1
                    plato.comprados +=1
                    plato.save()

            return HttpResponse(status=200)



