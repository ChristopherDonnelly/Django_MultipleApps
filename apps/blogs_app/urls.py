from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^([0-9]{1,})/$', views.show),
    url(r'^([0-9]{1,})/edit/$', views.edit),
    url(r'^([0-9]{1,})/delete/$', views.destroy)
]