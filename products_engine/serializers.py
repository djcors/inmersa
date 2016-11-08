# -*- coding: utf-8 -*-
from django.conf import settings
from rest_framework import serializers, renderers
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from .models import Plato

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )


class PlatoSerializer(serializers.ModelSerializer):

    usuario = UserSerializer(many=False, read_only=True)
    fav = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Plato
        fields = ('usuario', 'codigo', 'nombre', 'valor','activo',
            'descripcion', 'ingredientes', 'calorias', 'grasa','zona',
            'foto','fav','shared', 'comprados','stock','pk')


    
            