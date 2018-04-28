from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages import views

from rest_framework import routers

from apps.comments.api import CommentViewSet
from apps.posts.api import PostViewSet

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)

urlpatterns = [
    url(r'^manager/', admin.site.urls),
    url(r'^v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^comments/', include("apps.comments.urls", namespace='comments')),
    url(r'^martor/', include('martor.urls')),

]

urlpatterns += [
    url(r'^about-us/$', views.flatpage),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
