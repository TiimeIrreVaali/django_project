from django.urls import path
from core.views import *

urlpatterns = [
    path('', index),
    path('catalog/', catalog),
    path('news/', news),
]