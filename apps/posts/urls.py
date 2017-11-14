from django.conf.urls import url
from django.contrib import admin

# from django.contrib.flatpages import views
from django.conf.urls import (
    handler400, handler403, handler404, handler500
)

handler400 = 'posts.views.bad_request'
handler403 = 'posts.views.permission_denied'
handler404 = 'posts.views.page_not_found'
handler500 = 'posts.views.server_error'
from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
)

urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    # url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
