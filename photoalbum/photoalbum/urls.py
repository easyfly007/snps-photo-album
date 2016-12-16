# encoding: utf-8
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from photoapp import views as app

urlpatterns = [
    # Examples:
    # url(r'^$', 'photoalbum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', app.index),
    url(r'^index$', app.index),

    url(r'^post/(?P<postid>\d+)$', app.post),
    url(r'^post/(?P<postid>\d+)/edit$', app.post_edit),

    url(r'^tag/(?P<tagname>\w+)$', app.tag),

    # upload images    
    url(r'^upload$', app.upload),
    url(r'^uploading$', app.uploading),

    # see all the photos for one user
    url(r'^gallery/(?P<username>\w+)$', app.gallery),
    
    # see the profile of one user
    url(r'^profile/(?P<username>\w+)$', app.profile),
    url(r'^profile_edit/(?P<username>\w+)$', app.profile_edit),

    url(r'^login/', app.login_form),
    url(r'^logout$', app.logout_form),
    url(r'^register$', app.register),
    url(r'^logging$', app.logging),
    
    # ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

    