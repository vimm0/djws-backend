"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from blog.apps.accounts.views import (login_view, register_view, logout_view, user_detail_view)
from blog.apps.web_sikhshalaya.views import (about_view, sitemap_view, resource_view, contact_view, policy_view, terms_view)

from django.contrib.flatpages import views


urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^comments/', include("blog.apps.comments.urls", namespace='comments')),
    # accounts
    url(r'^register/', register_view, name='register'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
        url(r'^detail/', user_detail_view, name='detail'),

    # web_shikhshalaya
    url(r'^sitemap/', sitemap_view, name='sitemap'),
    url(r'^resource/', resource_view, name='resource'),
    url(r'^contact/', contact_view, name='contact'),
    url(r'^about/', about_view, name='about'),
    url(r'^terms/', terms_view, name='terms'),
    url(r'^policy/', policy_view, name='policy'),
    # url(r'^officeindex/', about_office_view, name='about_office'),

    #flat pages
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    #url(r'^posts/$', "<appname>.views.<function_name>"),

    url(r'^', include("blog.apps.posts.urls", namespace='posts')),

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