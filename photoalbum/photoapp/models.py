from django.db import models

# for user profile
class User(models.Model):
	username = models.CharField(max_length=32)
	nickname = models.CharField(max_length=32)
	pic = models.ImageField(upload_to = 'profile_pics/',default='profile_pics/default.jpg')
	info = models.TextField()
	friends = models.ManyToManyField('self', blank=True)
	blacklists = models.ManyToManyField('self', blank=True)
	administrator = models.BooleanField()
	locked = models.BooleanField()

	def __unicode__(self):
		return self.username

# same named tag from different user are actually different,
# think in condition somebody changed his tag name for one post, 
# other's post with same tag name should not be changed 
class Tag(models.Model):
	author = models.ForeignKey(User)
	title = models.CharField(max_length = 10)
	def __unicode__(self):
		return self.title

class Post(models.Model):
	author = models.ForeignKey(User)
	time = models.DateTimeField()
	title = models.CharField(max_length = 20)
	tag = models.ManyToManyField(Tag, blank=True)

	def __unicode__(self):
	    return self.title

	class Meta:
		ordering = ('-time',)

# no need to add user information in the Photo table, as we can find it through post 
class Photo(models.Model):
	title = models.CharField(max_length = 20)
	thumbnail = models.ImageField(upload_to = 'upload_pics/',default='upload_pics/default.jpg')
	# FileField only contains the root for the file 
	truesize  = models.ImageField(upload_to = 'upload_pics/',default='upload_pics/default.jpg')
	# true size photo url
	post = models.ForeignKey(Post, related_name = 'photos')
	tag = models.ManyToManyField(Tag,blank=True)
	iscoverpage = models.BooleanField

	def __unicode__(self):
	    return self.title

	class Meta:
		ordering = ('title',)

class Comment(models.Model):
	author = models.ForeignKey(User)
	time = models.DateTimeField
	content = models.TextField


class PostComment(Comment):
	post = models.ForeignKey(Post, related_name = 'comments')

class PhotoComment(Comment):
	photo = models.ForeignKey(Photo, related_name = 'comments')
