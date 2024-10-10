from django.http import HttpResponse
from django.shortcuts import render

def forum(request):
    return HttpResponse('Приложение forum, страница форума')

def user_profile(request):
    return HttpResponse('Приложение forum, страница профиля пользователя')

def topic(request):
    return HttpResponse('Приложение forum, страница тем')

def new_topic(request):
    return HttpResponse('Приложение forum, страница создания новой темы')
