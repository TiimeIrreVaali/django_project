from django.urls import path

from forum.views import *


app_name = 'forum'

urlpatterns = [
    #path('<slug:profile_slug>/', user_profile, name='user_profile'),
    path('', SubForumListView.as_view(), name='forum'),
    path('<slug:subforum_slug>/', TopicListView.as_view(), name='subforum'),
    path('<slug:subforum_slug>/add_topic/', AddTopic.as_view(), name="add_topic"),
    path('<slug:subforum_slug>/topics/<slug:topic_slug>/', ShowTopic.as_view(), name='topic'),
    path('<slug:subforum_slug>/topics/<slug:topic_slug>/add_comment/', AddComment.as_view(), name="add_comment"),
    path('<slug:subforum_slug>/topics/<slug:topic_slug>/<int:pk>/edit_comment/', UpdateComment.as_view(), name="edit_comment"),
    path('<slug:subforum_slug>/topics/<slug:topic_slug>/<int:pk>/delete_comment/', DeleteComment.as_view(), name="delete_comment"),
]
