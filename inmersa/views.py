# -*- coding: utf-8 -*-
import json
import simplejson
import requests
import datetime
from django import http
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import logout, login, authenticate
from django.views.generic import TemplateView
from django.template.response import TemplateResponse

def HomeView(request):
    return render(request, 'home.html', {})
