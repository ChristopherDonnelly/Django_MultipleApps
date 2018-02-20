from django.conf.urls import url 
from . import views 
 
urlpatterns = [
    url(r'^$', views.users),
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^users/new/$', views.new),
    url(r'^users/create/$', views.create),
    url(r'^users/update/([0-9]{1,})/$', views.update),
    url(r'^users/([0-9]{1,})/$', views.show),
    url(r'^users/([0-9]{1,})/edit/$', views.edit),
    url(r'^users/([0-9]{1,})/destroy/$', views.destroy)
] 
