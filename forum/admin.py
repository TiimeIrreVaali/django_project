from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import User, Profile, Subforum, Topic, Comment


class SubforumAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}


class TopicAdmin(admin.ModelAdmin):
    list_display = ['subject', 'creator', 'closed']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'author']


admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Subforum, SubforumAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment, CommentAdmin)
