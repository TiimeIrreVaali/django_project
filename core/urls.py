from django.urls import path
from .views import *  # точка означает исходную папку


urlpatterns = [path('', IndexPage.as_view(), name='home'),
               path('about', AboutPage.as_view(), name='about'),
               path('characters/', Characters.as_view(), name='characters'),
               path('episodes/', EpisodesPage.as_view(), name='episodes'),
               path('posts/<slug:post_slug>', ShowPost.as_view(), name='posts'),
               path('characters/<slug:char_slug>', ShowChar.as_view(), name='chars'),
               ]
