from django.shortcuts import get_object_or_404, render, render_to_response, get_list_or_404
from .models import *
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
# from django.contrib import comments
from django.http import Http404
from django.template import RequestContext
from .decorator import decorate
import os
from django.conf import settings
from PIL import Image


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
    post_list = get_list_or_404(Post)
    if Request.user.is_authenticated():
        print('is_authenticated is True')
    else:
        print('is_authenticated is False')

    return render_to_response('photoapp/index.html', locals())

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
@decorate
def upload(Request):
    return render_to_response(
        'photoapp/upload.html',
        RequestContext(Request,locals()))


@decorate
def uploading(Request):
    if Request.method != 'POST':
        return HttpResponseRedirect('/index')

    f = Request.FILES.get('fileList', None)
    if f is None:
        return HttpResponse('no image file uploaded')
    
    post_id = Request.POST.get('post_id', None)
    if post_id:
        post = Post.objects.get(pk = post_id)
    else:
        pass # TODO: create new post here


    # thumbnail = Image.open(f)
    # thumbnail.thumbnail((800, 800))
    # thumbnail.save('thumbnail.jpg', 'jpeg')

    # thumbnail.thumbnail((128, 128), Image.ANTIALIAS)

    # post = Post.objects.get(pk = post_id, None)
    photo = Photo(
        truesize = f, 
        # thumbnail= thumbnail, 
        post_id = post_id, 
        title = 'my image')
    photo.save()

    # baseDir = settings.MEDIA_ROOT
    # jpgdir = os.path.join(baseDir, 'upload_pics')
    # with open('C:\\Users\\yfhuang\\Desktop\programming\\snps-photo-album\\photoalbum\\upload_pics\\001.jpg', 'wb+') as destination:
    #         for chunk in uploadedfile.chunks():
    #             destination.write(chunk)
    

    # print str(photo.truesize)
    # basedir, imgefile = os.path.split(photo.truesize.path)
    # thumbnailname = os.path.join(basedir, 'thumb', imgefile)
    # thumbnail = Image.open(f)  
    # thumbnail.thumbnail((128,128), Image.ANTIALIAS)
    # thumbnail.save(thumbnailname)
    # photo.thumbnail = thumbnail
    # photo.save()

    return HttpResponse(photo.truesize.url)


@decorate
def gallery(Request, username):
    return render_to_response(
        'photoapp/index.html',
        RequestContext(Request,locals()))

@decorate
def profile(Request, username):
    return render_to_response(
        'photoapp/index.html',
        RequestContext(Request,locals()))


def login(Request):
    return render_to_response(
        'photoapp/login.html',
        RequestContext(Request,locals()))

def logout(Request):
    valid_user = Request.session.get('valid_user', False)
    if valid_user:
        del Request.session['valid_user']
    return HttpResponseRedirect('/login')

def logging(Request):
    if Request.method  == 'POST':
        if 'username' in Request.POST and Request.POST['username']:
            username = Request.POST['username']
            valid_user = dict()
            valid_user['username'] = username
            valid_user['userid'] = 12
            Request.session['valid_user'] = valid_user
            return HttpResponseRedirect('/index')
    return HttpResponseRedirect('/login')

def register(Request):
    return render_to_response(
        'photoapp/index.html',
        RequestContext(Request,locals()))

