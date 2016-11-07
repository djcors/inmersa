"""
Django settings for inmersa project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import dj_database_url
import psycopg2
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_PATH = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '03=s9^=&*5me1w%rzqsjc&yl7ra!+0vnrb+eqn4vgzj1wk&6%b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["localhost", "inmersa.herokuapp.com"]
ADMINS = [('Jonathan Cortes', 'djcors@gmail.com')]


# Application definition

INSTALLED_APPS = [
    'inmersa',
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'rest_framework',
    'products_engine',
    'shop_engine',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'inmersa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, "/templates/")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'inmersa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'inmersa',
        'USER': 'inmersa',
        'PASSWORD': 'Ewd-APM-T4C-CtD',
        'HOST': 'testinmersa1.clr9lus1fmqn.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }

}



db_from_env = dj_database_url.config(conn_max_age=1000)
DATABASES['default'] =  dj_database_url.config()
DATABASES['default'] =  dj_database_url.config(default='postgres://inmersa:Ewd-APM-T4C-CtD@testinmersa1.clr9lus1fmqn.us-east-1.rds.amazonaws.com:5432/inmersa')
DATABASES['default'].update(db_from_env)
DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'inmersa',
#        'USER': 'inmersa157',
#        'PASSWORD': 'pkay78KuysU]^cd',
#        'HOST': 'localhost',
#        'PORT': '',
#    },
#}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'es-CO'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = False

USE_TZ = False

SESSION_EXPIRE_AT_BROWSER_CLOSE = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication', 
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DATETIME_FORMAT': "%d-%m-%YT%I:%M %p",
}

#theme admin conf
SUIT_CONFIG = {
    'ADMIN_NAME': 'Tienda de platos'
}


AWS_S3_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY')
AWS_S3_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'inmersa'
SECRET_KEY = 'A long string with many different types of characters'


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'


STATIC_ROOT = os.path.join(BASE_PATH, 'static')
STATICFILES_DIRS = [
    #os.path.join(BASE_PATH, 'static'),

]
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_PATH, 'media')
MEDIA_URL = '/media/'
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
#date formats
DATE_FORMAT = 'j F Y'
TIME_FORMAT = 'H:i'
DATETIME_FORMAT = 'j F Y h:i'
YEAR_MONTH_FORMAT = 'F Y'
MONTH_DAY_FORMAT = 'j F'
SHORT_DATE_FORMAT = 'j N Y'
SHORT_DATETIME_FORMAT = 'j N Y H:i'
FIRST_DAY_OF_WEEK = 1


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

URL_API = "http://inmersa.corsdev.co/"

try:
    from .local_settings import *
except ImportError:
    pass

