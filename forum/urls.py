from django.urls import path

from forum.views import *

app_name = 'forum'

urlpatterns = [
    #path('<slug:profile_slug>/', user_profile, name='user_profile'),
    path('', SubForumListView.as_view(), name='forum'),
    path('<slug:subforum_slug>/', TopicListView.as_view(), name='subforum'),
    path('subforum/<slug:topic_slug>/', ShowTopic.as_view(), name='topic'),
    path('subforum/add-topic/', AddTopic.as_view(), name="add_topic"),
    path('subforum/<slug:topic_slug>/add-comment/', AddComment.as_view(), name="add_comment"),
    path('subforum/<slug:topic_slug>/edit/<int:id>/', UpdateComment.as_view(), name="edit_comment"),
]