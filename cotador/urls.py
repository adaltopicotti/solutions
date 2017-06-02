from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.quotation, name='quotation'),
    url(r'^cpf$', views.cpf, name='cpf'), 
]
