from django.contrib import admin
from photoapp.models import User, Post, Photo, Tag, Comment

class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'administrator', 'locked')

class PostAdmin(admin.ModelAdmin):
	pass

class PhotoAdmin(admin.ModelAdmin):
	pass

class TagAdmin(admin.ModelAdmin):
	pass

class CommentAdmin(admin.ModelAdmin):
	pass

# admin.site.register(User)
# admin.site.register(Post)
# admin.site.register(Photo)
# admin.site.register(Tag)
# admin.site.register(Comment)

admin.site.register(User, UserAdmin)
admin.site.register(Post, PhotoAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
