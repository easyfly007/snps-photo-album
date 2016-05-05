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
	

