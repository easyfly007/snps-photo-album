# encoding: utf-8
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'photoalbum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'photoapp.views.index'),
    url(r'^index$', 'photoapp.views.index'),
    # url(r'^login$', 'photoapp.views.login'),
    # url(r'^logout$', 'photoapp.views.logout'),

    url(r'^user/(?P<userid>\w+)$', 'photoapp.views.user'),
    url(r'^user/(?P<userid>\w+)/profile$', 'photoapp.views.profile'),
    url(r'^user/(?P<userid>\w+)/profile/edit$', 'photoapp.views.profile_edit'),

    url(r'^user/(?P<userid>\w+)/new$',    'photoapp.views.user_new'),
    url(r'^user/(?P<userid>\w+)/edit$',   'photoapp.views.user_edit'),
    # url(r'^user/(?P<userid>\w+)/delete$', 'photoapp.views.user_delete'),

    # url(r'^user/(?P<userid>\w+)/post/(?P<postid>\d+)$', 'photoapp.views.post'),
    # url(r'^user/(?P<userid>\w+)/post/(?P<postid>\d+)/edit$', 'photoapp.views.post_edit'),
    url(r'^post/(?P<postid>\d+)$', 'photoapp.views.post'),
    url(r'^post/(?P<postid>\d+)/edit$', 'photoapp.views.post_edit'),
 

    # url(r'^user/(?P<userid>\w+)/post/(?P<postid>\d+)/photo/(?P<photoid>)\d+$', 'photoapp.views.photo'),
    # url(r'^user/(?P<userid>\w+)/post/(?P<postid>\d+)/photo/(?P<photoid>)\d+/edit$', 'photoapp.views.photo_edit'),
    url(r'^post/(?P<postid>\d+)/photo/(?P<photoid>\d+)$', 'photoapp.views.photo'),
    url(r'^post/(?P<postid>\d+)/photo/(?P<photoid>\d+)/edit$', 'photoapp.views.photo_edit'),

    # TODO 
    # tag
    # url(r'^post/(?P<postid>\d+)/photo/(?P<photoid>)\d+/edit$', 'photoapp.views.photo_edit'),    
    # event 比赛评选 vote
    # gallery 个人收藏
    
    url(r'^upload$', 'photoapp.views.upload'),
    url(r'^uploading$', 'photoapp.views.uploading'),

    # see all the photos for one user
    url(r'^gallery/(?P<username>\w+)$', 'photoapp.views.gallery'),
    # see the profile of one user
    url(r'^profile/(?P<username>\w+)$', 'photoapp.views.profile'),

    url(r'^login$', 'photoapp.views.login'),
    url(r'^logout$', 'photoapp.views.logout'),
    url(r'^register$', 'photoapp.views.register'),
    url(r'^logging$', 'photoapp.views.logging'),
    
    # ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

    