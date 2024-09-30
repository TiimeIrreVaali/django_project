from django.urls import path
from root.views import *

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('user_page/', user_page),
]