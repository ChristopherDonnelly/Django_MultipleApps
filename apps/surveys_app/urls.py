from django.conf.urls import url 
from . import views 
 
urlpatterns = [ 
    url(r'^$', views.index),
    url(r'^new/$', views.new),
    url(r'^process_form/$', views.process_form),
    url(r'^results/$', views.results),
    url(r'^back/$', views.back)
] 
