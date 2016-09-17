from django.shortcuts import get_object_or_404, render, render_to_response, get_list_or_404
from .models import *
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
# from django.contrib import comments
from django.http import Http404
from django.template import RequestContext

    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^$/', 'photoapp.views.index'),
    # url(r'^index$/', 'photoapp.views.index'),
    # url(r'^login$/', 'photoapp.views.login'),
    # url(r'^logout$/', 'photoapp.views.logout'),

    # url(r'^user_(?P<userid>\w+)$/', 'photoapp.views.user'),
    # url(r'^user_(?P<userid>\w+)/profile$/', 'photoapp.views.profile'),
    # url(r'^user_(?P<userid>\w+)/profile/edit$/', 'photoapp.views.profile_edit'),

    # url(r'^user_(?P<userid>\w+)/new$/',    'photoapp.views.user_new'),
    # url(r'^user_(?P<userid>\w+)/edit$/',   'photoapp.views.user_edit'),
    # url(r'^user_(?P<userid>\w+)/delete$/', 'photoapp.views.user_delete'),

    # url(r'^user_(?P<userid>\w+)/post_(?P<postid>\d+)$/', 'photoapp.views.post'),
    # url(r'^user_(?P<userid>\w+)/post_(?P<postid>\d+)/edit$/', 'photoapp.views.post_edit'),

    # url(r'^user_(?P<userid>\w+)/post_(?P<postid>\d+)/photo_(?P<photoid>)\d+$/', 'photoapp.views.photo'),
    # url(r'^user_(?P<userid>\w+)/post_(?P<postid>\d+)/photo_(?P<photoid>)\d+/edit$/', 'photoapp.views.photo_edit'),

 # main page, show all the post with by time line
def index(Request):
    cur_post = get_list_or_404(Post)
    print cur_post
    return render_to_response('photoapp/index.html', {'post_list': cur_post})
	# return HttpResponse("index page")

def login(Request):
	return HttpResponse('login page')

def logout(Request):
	return HttpResponse('log out page')


def user(Request, userid):
	return HttpResponse('user page with userid='+userid)

def profile(Request, userid):
    return render_to_response('photoapp/userprofile/index.html', locals())
	# return HttpResponse('user profile page')

def profile_edit(Request, userid):
	return HttpResponse('user profile edit page')


def user_new(Request, userid):
	return HttpResponse('user new post page')
def user_edit(Request, userid):
	return HttpResponse('user edit post page')
def user_delete(Request, userid):
	return HttpResponse('user delete post page')



def post(Request, postid):
    cur_post = get_object_or_404(Post, pk=postid)
    print cur_post
    return render_to_response('photoapp/post_detail.html', {'post': cur_post})

def post_edit(Request, postid):
	return HttpResponse('user post  edit page')


def photo(Request, postid, photoid):
    cur_post = get_object_or_404(Post, pk=postid)
    cur_photo = get_object_or_404(Photo, pk=photoid)
    return render_to_response('photoapp/photo.html', {'post': cur_post, 'photo': cur_photo})

def photo_edit(Request, userid, postid, photoid):
	return HttpResponse('user post photo edit page')



# show page for user upload photos
def upload(Request):
    valid_user = dict()
    valid_user['username'] = 'yfhuang'
    valid_user['userid'] = 12
    Request.session['valid_user'] = valid_user
    return render_to_response(
        'photoapp/upload.html',
        RequestContext(Request,locals()))

def uploading(Request):
    # TODO: processing uploaded photos
    return render(Request,'photoapp/index.html',locals())

def gallery(Request, username):
    return render_to_response(
        'photoapp/index.html',
        RequestContext(Request,locals()))

def profile(Request, username):
    return render_to_response(
        'photoapp/index.html',
        RequestContext(Request,locals()))

def login(Request):
    return render_to_response(
        'photoapp/index.html',
        RequestContext(Request,locals()))

def register(Request):
    return render_to_response(
        'photoapp/index.html',
        RequestContext(Request,locals()))    