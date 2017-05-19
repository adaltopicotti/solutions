from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.quotation, name='quotation'),
    url(r'^$', views.city_list, name='city_list'),
]
