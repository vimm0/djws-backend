from django.conf.urls import url
from django.contrib import admin

from apps.accounts.views import (login_view, register_view, logout_view, user_detail_view, activate)

urlpatterns = [
    # accounts
    url(r'^signup/', register_view, name='signup'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^detail/', user_detail_view, name='detail'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate, name='activate'),
]
