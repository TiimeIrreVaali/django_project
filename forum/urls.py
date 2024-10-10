from django.urls import path
from forum.views import *

urlpatterns = [
    path('forum/<slug:profile_slug>', user_profile, name='user_profile'),
    path('forum/<str:name>/', forum, name='subforum'),
    path('forum/subforum/<slug:topic_slug>/', topic, name='topic'),
    path('forum/subforum/topic/<slug:comment_slug>/', topic, name='comment'),
    path('new_topic/', new_topic),
]