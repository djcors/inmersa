#! coding: utf-8
import os
import multiprocessing

os.environ['DJANGO_SETTINGS_MODULE'] = 'inmersa.settings'
short_name = "inmersa"

bind      = "unix:/var/run/django/%s.sock" % short_name
proc_name = "/var/run/django/%s" % short_name
workers = multiprocessing.cpu_count() * 2 + 1

user      = "ubuntu"
group     = "www-data"
loglevel  = "warn"
timeout   = 600
keepalive = 5
