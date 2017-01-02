from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# same named tag from different user are actually different,
# think in condition somebody changed his tag name for one post, 
# other's post with same tag name should not be changed 
class Tag(models.Model):
	author = models.ForeignKey(User)
	title = models.CharField(max_length = 80)
	def show_name(self):
		return self.title.replace('_', ' ')
	def unique_name(self):
		return self.title


class Post(models.Model):
	author = models.ForeignKey(User)
	time = models.DateTimeField()
	title = models.CharField(max_length = 20)
	tag = models.ManyToManyField(Tag, related_name = 'posts', blank=True)

	def __unicode__(self):
	    return self.title

	class Meta:
		ordering = ('-time',)

# no need to add user information in the Photo table, as we can find it through post 
class Photo(models.Model):
	title = models.CharField(max_length = 20)
	# thumbnail = models.ImageField(upload_to = 'upload_pics/',default='upload_pics/default.jpg')
	# FileField only contains the root for the file 
	truesize  = models.ImageField(upload_to = 'upload_pics/',default='upload_pics/default.jpg')
	width = models.IntegerField(default = 0)
	height = models.IntegerField(default = 0)
	# true size photo url
	post = models.ForeignKey(Post, related_name = 'photos')
	tag = models.ManyToManyField(Tag, related_name = 'photos', blank=True)
	iscoverpage = models.BooleanField

	def __unicode__(self):
	    return self.title

	def tags(self):
	    return self.tag.all()

	class Meta:
	    ordering = ('title',)

class Comment(models.Model):
	author = models.ForeignKey(User)
	time = models.DateTimeField(default=datetime.now)
	content = models.CharField(max_length=1024)


class PostComment(Comment):
	post = models.ForeignKey(Post, related_name = 'comments')

class PhotoComment(Comment):
	photo = models.ForeignKey(Photo, related_name = 'comments')
