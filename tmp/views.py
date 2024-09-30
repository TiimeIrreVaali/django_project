from django.http import HttpResponse
from django.shortcuts import render

def forum(request):
    return HttpResponse('Приложение tmp, страница форума')

def vote(request):
    return HttpResponse('Приложение tmp, страница голосований')

def new_topic(request):
    return HttpResponse('Приложение tmp, страница создания новой темы')
