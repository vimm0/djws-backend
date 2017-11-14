from django.conf.urls import url
from django.contrib import admin

from apps.accounts.views import (login_view, register_view, logout_view, user_detail_view)

urlpatterns = [
    # accounts
    url(r'^register/', register_view, name='register'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^detail/', user_detail_view, name='detail'),

]
