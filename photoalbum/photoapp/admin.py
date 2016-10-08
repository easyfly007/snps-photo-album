from django.contrib import admin
from photoapp.models import Post, Photo, Tag, Comment

# class UserAdmin(admin.ModelAdmin):
# 	list_display = ('username', 'nickname', 'administrator', 'locked')
	
class PostAdmin(admin.ModelAdmin):
	list_display = ('author', 'time', 'tag', 'title')
	list_filter = ('author', 'tag')

class PhotoAdmin(admin.ModelAdmin):
	list_display = ('title', )
	list_filter = ('tag',)

class TagAdmin(admin.ModelAdmin):
	list_display= ('author', 'title',)
	list_filter = ('author',)

class CommentAdmin(admin.ModelAdmin):
	list_display = ('time', 'content')


# admin.site.register(User, UserAdmin)
admin.site.register(Post, PhotoAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
