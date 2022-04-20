from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    url(r'^concept$', views.concept),
    url(r'^actus/$', views.actus),
    url(r'^contact/$', views.contact),
    url(r'^produits/$', views.produits),
    url(r'^(?P<actu_id>[0-9]+)/$', views.detailActu),
    url(r'^article-produit$', views.detailProduit),
]