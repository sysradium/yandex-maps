try:
    from django.conf.urls import url, include
except ImportError:
    from django.conf.urls.defaults import *

try:
    from django.shortcuts import render
except ImportError:
    from django.views.generic.simple import direct_to_template as render

from django.views.generic import TemplateView

urlpatterns = [
    url(r'^yandex/', include('yandex_maps.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index')
]
