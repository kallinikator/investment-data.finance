from django.conf.urls import url
from . import views

app_name = 'api' # This is a namespace to seperate different names to use as {% url "namespace:name" addition %}

urlpatterns = [
    url(r'^$', views.list_view, name = 'list_view'),
	url(r'^(?P<symbol>[A-Z]{,5})$', views.detail_view, name = 'detail_view'),
    ]