from django.shortcuts import get_object_or_404, render, render_to_response, get_list_or_404
from .models import *
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
# from django.contrib import comments
from django.http import Http404
from django.template import RequestContext
import os
from django.conf import settings
from PIL import Image

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from datetime import datetime

@login_required
def index(Request):
    post_list = get_list_or_404(Post)
    return render_to_response('photoapp/index.html', locals())

def profile(Request, userid):
    return render_to_response('photoapp/userprofile/index.html', locals())

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


@login_required
def photo(Request, postid, photoid):
    post = get_object_or_404(Post, pk=postid)
    photo = get_object_or_404(Photo, pk=photoid)
    content = Request.POST.get('comment_content', None)
    if content:
        newComment = PhotoComment(author = Request.user, time=datetime.now().replace(microsecond=0), photo=photo, content=content)
        newComment.save()
    return render_to_response('photoapp/photo.html', RequestContext(Request, locals()) )

def photo_edit(Request, userid, postid, photoid):
	return HttpResponse('user post photo edit page')



# show page for user upload photos
@login_required
def upload(Request):
    return render_to_response(
        'photoapp/upload.html',
        RequestContext(Request,locals()))


@login_required
def uploading(Request):
    if Request.method != 'POST':
        return HttpResponseRedirect('/index')

    f = Request.FILES.get('fileList', None)
    if f is None:
        return HttpResponse('no image file uploaded')
    
    post = None
    newpost = Request.POST.get('newpost', None)
    if newpost and int(newpost) == 0:
        last_postid = Request.session.get('last_postid', None)
        if last_postid:
            post = Post.objects.get(pk = last_postid)
    if post is None:
        post = Post(author = Request.user, title='', time=datetime.now() )
        post.save()
        Request.session['last_postid'] = post.id

    photo = Photo(
        truesize = f, 
        post = post, 
        title = 'my image')
    photo.save()
    return HttpResponse(photo.truesize.url)


@login_required
def gallery(Request, username):
    user = User.objects.get(username = username)
    post_list = user.post_set.all()
    return render_to_response(
        'photoapp/index.html',
        RequestContext(Request,locals()))

@login_required
def profile(Request, username):
    return render_to_response(
        'photoapp/index.html',
        RequestContext(Request,locals()))


def login_form(Request):
    return render_to_response(
        'photoapp/login.html',
        RequestContext(Request, locals()))

def logout_form(Request):
    logout(Request)
    return HttpResponseRedirect('/login')

def logging(Request):
    if Request.method  == 'POST':
        username = Request.POST['username']
        password = Request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                login(Request, user)
                # print("User is valid, active and authenticated")
                return HttpResponseRedirect('/index')
            else:
                pass
                # print("The password is valid, but the account has been disabled!")
        else:
            pass
            # the authentication system was unable to verify the username and password
            # print("The username and password were incorrect.")
    return HttpResponseRedirect('/login')

def register(Request):
    return render_to_response(
        'photoapp/index.html',
        RequestContext(Request,locals()))

