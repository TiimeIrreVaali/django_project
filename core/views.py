from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Добро пожаловать на главную страницу сайта N!')

def catalog(request):
    return HttpResponse('Приложение core, страница каталога')

def news(request):
    return HttpResponse('Приложение core, страница новостей')
