from django.urls import path
from tmp.views import *

urlpatterns = [
    path('forum/', forum),
    path('vote/', vote),
    path('new_topic/', new_topic),
]