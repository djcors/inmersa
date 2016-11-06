# -*- coding: utf-8 -*-
import json
import simplejson
import requests
import datetime
from django import http
from django.http import HttpResponseNotAllowed, HttpResponseNotFound, HttpResponse, HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.template.response import TemplateResponse
from django.template import RequestContext

def HomeView(request):
    if request.user.is_authenticated():
        url = "http://localhost:8000/api/platos"
        headers = {'Accept':'application/json'} 
        r = requests.get(url, headers=headers)
        recibe = r.json()
        for plato in recibe:
            for fav in plato["fav"]:
                if request.user.username == fav["username"]:
                    plato['liked'] = True
        response = render(request, "home.html", {'platos':recibe,})
        return response
    else:
        return render(request, 'home.html', {})


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

