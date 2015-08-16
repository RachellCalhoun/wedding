"""weddingsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static 
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^registry/', include('registry.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rsvp/', include('rsvp.urls')),
    url(r'^photos/', include('photos.urls')),
    url(r'^home/',TemplateView.as_view(template_name='staticsites/home.html'),name='home'),
    
    url(r'^ourstory/',TemplateView.as_view(template_name='staticsites/ourstory.html'),name='ourstory'),
    url(r'^info/',TemplateView.as_view(template_name='staticsites/info.html'),name='info'),
    url(r'^$',TemplateView.as_view(template_name='staticsites/home.html'),name='home'),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

