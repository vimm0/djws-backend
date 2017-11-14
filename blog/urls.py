from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from django.contrib.flatpages import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # flat pages
    url(r'^pages/', include('django.contrib.flatpages.urls')),

    # Apps
    url(r'^', include("apps.accounts.urls", namespace='accounts')),
    url(r'^comments/', include("apps.comments.urls", namespace='comments')),
    url(r'^', include("apps.posts.urls", namespace='posts')),
    url(r'^', include("apps.web_sikhshalaya.urls", namespace='web_sikhshalaya')),
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
