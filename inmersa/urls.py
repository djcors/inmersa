"""inmersa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include, patterns, handler404
from django.contrib import admin
from products_engine import urls as platos_urls 
from shop_engine import urls as shop_urls 
from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(platos_urls)),
    url(r'^api/', include(shop_urls)),
    url(r'^$', 'inmersa.views.HomeView', name='home'),
    url(r'^registro/$', 'inmersa.views.Register', name="Register"),
    url(r'^miscompras/$', 'inmersa.views.miscompras', name="miscompras"),
    url(r'^login/$', 'inmersa.views.LogIn', name="Login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': 'home'})


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
