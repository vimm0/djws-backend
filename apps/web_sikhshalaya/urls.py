from django.conf.urls import url
from django.contrib import admin

from .views import (about_view, sitemap_view, resource_view, contact_view, policy_view, terms_view)

urlpatterns = [
    url(r'^about/', about_view, name='about'),
    url(r'^terms/', terms_view, name='terms'),
    url(r'^policy/', policy_view, name='policy'),
    url(r'^sitemap/', sitemap_view, name='sitemap'),
    url(r'^resource/', resource_view, name='resource'),
    url(r'^contact/', contact_view, name='contact'),
]
