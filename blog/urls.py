from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.list_view, name = 'list_view'),
	url(r'^(?P<id>[0-9]+)$', views.detail_view, name = 'detail_view')
    ]