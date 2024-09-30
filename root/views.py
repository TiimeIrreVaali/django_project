from django.http import HttpResponse
from django.shortcuts import render

def register(request):
    return HttpResponse('Приложение root, страница регистрации')

def login(request):
    return HttpResponse('Приложение root, страница авторизации')

def user_page(request):
    return HttpResponse('Приложение root, страница пользователя')
