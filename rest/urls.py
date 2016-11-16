from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Stock_list),
    url(r'^(?P<symbol>[A-Z]{,5})/$', views.Stock_detail),
]
