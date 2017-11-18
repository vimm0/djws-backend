from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^about/', views.AboutList.as_view(), name='about'),
    url(r'^terms/', views.TermList.as_view(), name='terms'),
    url(r'^policy/', views.PolicyList.as_view(), name='policy'),
    url(r'^sitemap/', views.SitemapList.as_view(), name='sitemap'),
    url(r'^resource/', views.ResourceList.as_view(), name='resource'),
    url(r'^contact/', views.ContactList.as_view(), name='contact'),
]
