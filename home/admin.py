from django.contrib import admin
from .models import Post, Comment, Like

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user','title', 'updated')
    list_filter = ('user','title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('content',)}
    date_hierarchy = 'updated'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'reply', 'is_reply')
    raw_id_fields = ('user', 'post', 'reply')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass