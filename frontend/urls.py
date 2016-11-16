from django.conf.urls import url
from . import views

app_name = 'frontend'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^terms', views.terms, name = 'terms'),
    url(r'^contact', views.contact, name = 'contact'),
    ]
