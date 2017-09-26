from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.quotation, name='quotation'),
    url(r'^pdc/$', views.pdc, name='pdc'),
    url(r'^pdc/add/$', views.add, name='add'),
    url(r'^pdc/weather/$', views.weather, name='weather'),
    url(r'^quotation/new/$', views.quotation_new, name='quotation_new'),
]
