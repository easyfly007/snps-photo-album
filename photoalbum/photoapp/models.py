from django.db import models

# for user profile
class User(models.Model):
	username = models.CharField(max_length=32)
	nickname = models.CharField(max_length=32)
	pic = models.ImageField(upload_to = 'profile_pics/',default='profile_pics/default.jpg')
	info = models.TextField()
	friends = models.ManyToManyField('self')
	blacklists = models.ManyToManyField('self')
	administrator = models.BooleanField()
	locked = models.BooleanField()

# same named tag from different user are actually different,
# think in condition somebody changed his tag name for one post, 
# other's post with same tag name should not be changed 
class Tag(models.Model):
	author = models.ForeignKey(User)
	title = models.CharField(max_length = 10)

class Post(models.Model):
	author = models.ForeignKey(User)
	time = models.TimeField()
	title = models.CharField(max_length = 20)
	tag = models.ManyToManyField(Tag)

# no need to add user information in the Photo table, as we can find it through post 
class Photo(models.Model):
	thumbnail = models.CharField(max_length = 60)
	truesize  = models.CharField(max_length = 60)
	post = models.ForeignKey(Post)
	tag = models.ManyToManyField(Tag)

class Comment(models.Model):
	author = models.ForeignKey(User)
	content = models.CharField(max_length = 140)

class PostComment(Comment):
	post = models.ForeignKey(Post)

class PhotoComment(Comment):
	photo = models.ForeignKey(Photo)
