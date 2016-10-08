# encoding: utf-8
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
import settings

from photoapp import views as app

urlpatterns = [
    # Examples:
    # url(r'^$', 'photoalbum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', app.index),
    url(r'^index$', app.index),
    # url(r'^login$', 'photoapp.views.login'),
    # url(r'^logout$', 'photoapp.views.logout'),

    url(r'^user/(?P<userid>\w+)$', app.user),
    url(r'^user/(?P<userid>\w+)/profile$', app.profile),
    url(r'^user/(?P<userid>\w+)/profile/edit$', app.profile_edit),

    url(r'^user/(?P<userid>\w+)/new$',    app.user_new),
    url(r'^user/(?P<userid>\w+)/edit$',   app.user_edit),
    # url(r'^user/(?P<userid>\w+)/delete$', 'photoapp.views.user_delete'),

    # url(r'^user/(?P<userid>\w+)/post/(?P<postid>\d+)$', 'photoapp.views.post'),
    # url(r'^user/(?P<userid>\w+)/post/(?P<postid>\d+)/edit$', 'photoapp.views.post_edit'),
    url(r'^post/(?P<postid>\d+)$', app.post),
    url(r'^post/(?P<postid>\d+)/edit$', app.post_edit),
 

    # url(r'^user/(?P<userid>\w+)/post/(?P<postid>\d+)/photo/(?P<photoid>)\d+$', 'photoapp.views.photo'),
    # url(r'^user/(?P<userid>\w+)/post/(?P<postid>\d+)/photo/(?P<photoid>)\d+/edit$', 'photoapp.views.photo_edit'),
    url(r'^post/(?P<postid>\d+)/photo/(?P<photoid>\d+)$', app.photo),
    url(r'^post/(?P<postid>\d+)/photo/(?P<photoid>\d+)/edit$', app.photo_edit),

    # TODO 
    # tag
    # url(r'^post/(?P<postid>\d+)/photo/(?P<photoid>)\d+/edit$', 'photoapp.views.photo_edit'),    
    # event 比赛评选 vote
    # gallery 个人收藏
    
    url(r'^upload$', app.upload),
    url(r'^uploading$', app.uploading),

    # see all the photos for one user
    url(r'^gallery/(?P<username>\w+)$', app.gallery),
    # see the profile of one user
    url(r'^profile/(?P<username>\w+)$', app.profile),

    url(r'^login/', app.login_form),
    url(r'^logout$', app.logout),
    url(r'^register$', app.register),
    url(r'^logging$', app.logging),
    
    # ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

    