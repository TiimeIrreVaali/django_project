from django.contrib import admin
from .models import User, Profile, Subforum, Topic, Comment


class SubforumAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}


class TopicAdmin(admin.ModelAdmin):
    list_display = ['subject', 'creator', 'closed']
    prepopulated_fields = {"slug": ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'author']
    prepopulated_fields = {"slug": ('title',)}


admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Subforum)
admin.site.register(Topic)
admin.site.register(Comment)
