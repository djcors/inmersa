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
from .models import Plato
from django.contrib.auth.models import User
from .serializers import PlatoSerializer
from django.views.decorators.csrf import csrf_exempt


class PlatoViewSet(generics.ListAPIView):
    serializer_class = PlatoSerializer
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self):
        queryset = Plato.objects.filter(activo=True)
        valid = {}
        for key, value in self.request.query_params.items():
            valid[key] = value
        queryset = queryset.filter(**valid)
        return queryset

Platos = PlatoViewSet.as_view()

@csrf_exempt
def fav_button(request):
    if request.method == "POST":
        user = User.objects.get(pk=request.POST['user'])
        plato = Plato.objects.get(pk=request.POST['plato'])
        if request.POST['liked']:
            plato.fav.remove(user)
            plato.liked = False
        else :
            plato.fav.add(user)
            plato.liked = True

        data = {
            'liked':plato.liked,
            'fav':plato.fav.count()
        }

        #serialized_obj = serializers.serialize('json', [ data, ])

    return HttpResponse(json.dumps(data), content_type="application/json")

