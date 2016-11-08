# -*- coding: utf-8 -*-
import json
import simplejson
import requests
import datetime
from django import http
from django.conf import settings
from django.http import HttpResponseNotAllowed, HttpResponseNotFound, HttpResponse, HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.template.response import TemplateResponse
from django.template import RequestContext
from shop_engine.models import Compra
from products_engine.models import Plato

def HomeView(request):
    if request.user.is_authenticated():
        url = settings.URL_API + "api/platos/"
        headers = {'Accept':'application/json'} 
        r = requests.get(url, headers=headers)
        recibe = r.json()
        todos_platos = []
        for plato in recibe:
            for fav in plato["fav"]:
                if request.user.username == fav["username"]:
                    todos_platos.append(plato)
                    plato['liked'] = True
        request.session.update({'likes':todos_platos})
        response = render(request, "home.html", {'platos':recibe,})
        return response
    else:
        return render(request, 'home.html', {})

def plato(request, codigo):
    if request.user.is_authenticated():
        url = settings.URL_API + "api/platos/?codigo="+codigo
        headers = {'Accept':'application/json'} 
        r = requests.get(url, headers=headers)
        recibe = r.json()

    return render(request, 'home.html', {'platos':recibe})


def Register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        
    return render_to_response('registro.html', {
        'form': form,
        }, context_instance=RequestContext(request))

def logout(request):
    logout(request)
    return redirect('home')

def LogIn(request):
    if request.method != 'POST':
        raise http.Http404
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('home')
        else:
            return redirect('/')
    else:
        return redirect('/?login=false')

def miscompras(request):
    if request.user.is_authenticated():
        compras = Compra.objects.filter(usuario=request.user)
        return render(request, 'miscompras.html', {'compras':compras})  

    return redirect('home')  

def misplatos(request):
    if request.user.is_authenticated():
        platos = Plato.objects.filter(usuario=request.user)
        return render(request, 'misplatos.html', {'platos':platos}) 
    return redirect('home')

def crear_plato(request):
    if request.user.is_authenticated():

        if request.method == 'POST':
            print('------')
            plato = Plato.objects.create(
                usuario=request.user,
                codigo=request.POST['codigo'],
                nombre=request.POST['nombre'],
                valor=request.POST['valor'],
                activo=request.POST['activo'],
                descripcion=request.POST['descripcion'],
                calorias=request.POST['calorias'],
                grasa=request.POST['grasa'],
                zona=request.POST['zona'],
                foto=request.FILES['foto'],
                ingredientes=request.POST['ingredientes'],
                stock=request.POST['stock'],
            )
            plato.save()
            return render(request, 'crear_plato.html', {'status':'ok'})
        return render(request, 'crear_plato.html', {})
    return redirect('home')

