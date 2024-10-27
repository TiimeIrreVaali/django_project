"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from forum.views import *


# класс для создания URL-маршрутов для viewset
router = DefaultRouter()
# для автоматической маршрутизации URL-адресов для vievset
router.register('topicsapi', TopicAPI, "topicsapi")
router.register('commentsapi', CommentAPI, "commentsapi")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name="schema"),
    path('swagger/', SpectacularSwaggerView.as_view(url_name="schema")),
    path('', include('core.urls')),
    path('news/', include('core.urls')),
    path('users/', include('users.urls', namespace="users")),
    path('user_page/', include('users.urls')),
    path('forum/', include('forum.urls', namespace="forum")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + router.urls
