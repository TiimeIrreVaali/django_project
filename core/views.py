from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import ListView, TemplateView, DetailView
from .models import *


menu = ['Главная страница', 'О проекте', 'Персонажи', 'Список серий', 'Форум', 'Войти', 'Время']


class IndexPage(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        posts = News.objects.filter(is_published=1)
        context = {'title': 'Главная страница', 'menu': menu, 'news': posts}
        return context


class AboutPage(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = {'title': "О проекте", 'menu': menu}
        return context


#@login_required
class Characters(ListView):
    model = Character
    context_object_name = "characters"
    template_name = 'core/chars.html'

    def get_context_data(self, **kwargs):
        chars = Character.objects.all()
        outers = Character.objects.filter(faction='outers')
        resistance = Character.objects.filter(faction='resistance')
        neutrals = Character.objects.filter(faction='neutrals')
        domination = Character.objects.filter(faction='domination')
        moon = Character.objects.filter(faction='moon')
        context = {'title': "Персонажи",
                   'menu': menu,
                   'characters': chars,
                   'outers': outers,
                   'resistance': resistance,
                   'neutrals': neutrals,
                   'domination': domination,
                   'moon': moon}
        return context


#@login_required
class EpisodesPage(TemplateView):
    model = Episode
    context_object_name = "episodes"
    template_name = 'core/episodes.html'

    def get_context_data(self, **kwargs):
        episodes = Episode.objects.all()
        context = {'title': "Список серий", 'menu': menu, 'episodes': episodes}
        return context


class ShowPost(TemplateView):
    model = News
    context_object_name = "posts"
    template_name = 'core/post.html'

    def get_context_data(self, post_slug, **kwargs):
        post = get_object_or_404(News, slug=post_slug)
        context = {'title': post.title, 'menu': menu, 'post': post}
        return context


class ShowChar(TemplateView):
    model = Character
    context_object_name = "chars_details"
    template_name = 'core/character_info.html'

    def get_context_data(self, char_slug, **kwargs):
        char = get_object_or_404(Character, slug=char_slug)
        context = {'name': char.name, 'type': char.type, 'description': char.description, 'char': char}
        return context


#def index(request):
#    posts = News.objects.filter(is_published=1)
#    data = {'title': 'Главная страница', 'menu': menu, 'news': posts}
#    return render(request, template_name='core/index.html', context=data)

#def about(request):
#    return render(request, 'core/about.html', {'menu': menu, 'title': "О проекте"})

#def characters(request):
#    chars = models.Character.objects.all()
##    factions = [Character.FACTION_CHOICES[i][0] for i in range(len(Character.FACTION_CHOICES))]
#    outers = models.Character.objects.filter(faction='outers')
#    resistance = models.Character.objects.filter(faction='resistance')
#    neutrals = models.Character.objects.filter(faction='neutrals')
#    domination = models.Character.objects.filter(faction='domination')
#    moon = models.Character.objects.filter(faction='moon')
#    data = {'title': "Персонажи",
#            'menu': menu,
#            'characters': chars,
#            'outers': outers,
#            'resistance': resistance,
#            'neutrals': neutrals,
#            'domination': domination,
#            'moon': moon}
#    return render(request, 'core/chars.html', context=data)

#def episodes(request):
#    context = {'menu': menu, 'title': "Список серий"}
#    return render(request, 'core/episodes.html', context=context)

#def pageNotFound(request, exception):
#    return HttpResponseNotFound('<h1>Страница не найдена!</h1>')

#def show_post(request, post_slug):
#    post = get_object_or_404(models.News, slug=post_slug)
#    data = {'title': post.title, 'menu': menu, 'post': post}
#    return render(request, "core/post.html", context=data)

#def show_char(request, char_slug):
#    char = get_object_or_404(models.Character, slug=char_slug)
#    data = {'name': char.name, 'description': char.description, 'char': char}
#    return render(request, "core/character_info.html", context=data)
