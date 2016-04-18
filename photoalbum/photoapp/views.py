from django.shortcuts import render, render_to_response
import models
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
# from django.contrib import comments
from django.contrib.auth.models import User


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

def index(Request):
	return HttpResponse("index page")

def login(Request):
	return HttpResponse('login page')

def logout(Request):
	return HttpResponse('log out page')


def user(Request, userid):
	return HttpResponse('user page with userid='+userid)

def profile(Request, userid):
	return HttpResponse('user profile page')

def profile_edit(Request, userid):
	return HttpResponse('user profile edit page')


def user_new(Request, userid):
	return HttpResponse('user new post page')
def user_edit(Request, userid):
	return HttpResponse('user edit post page')
def user_delete(Request, userid):
	return HttpResponse('user delete post page')



def post(Request, userid, postid):
	return HttpResponse('user post page')
def post_edit(Request, userid, postid):
	return HttpResponse('user post  edit page')


def photo(Request, userid, postid, photoid):
	return HttpResponse('user post photo page')

def photo_edit(Request, userid, postid, photoid):
	return HttpResponse('user post photo edit page')