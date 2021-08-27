from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^about$', views.about),
    url(r'^notes$', views.notes),
    url(r'^locations$', views.locations),
    url(r'^account$', views.account),
    url(r'^search$', views.search),
    url(r'^cart$', views.cart),
    url(r'^create_user$', views.create_user),
 
]

