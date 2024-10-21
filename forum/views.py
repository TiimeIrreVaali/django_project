from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from core.views import menu
from .forms import AddTopicForm, AddCommentForm
from .models import Subforum, Topic, Comment, Profile
from .utils import DataMixin


class SubForumListView(ListView):
    model = Subforum
    context_object_name = 'subforum_list'
    template_name = "forum/forum.html"

    def get_context_data(self, **kwargs):
        subforums = Subforum.objects.all()
        context = {'subforums': subforums}
        return context


class TopicListView(ListView):
    model = Topic
    template_name = "forum/subforum.html"
    slug_url_kwarg = 'subforum_slug'
    context_object_name = 'subforum'

    def get_context_data(self, **kwargs):
        topics = Topic.objects.all()
        context = {'topics': topics}
        return context


class ShowTopic(DetailView):
    model = Topic
    template_name = "forum/topic.html"
    slug_url_kwarg = 'topic_slug'
    context_object_name = 'topic'

    def get_context_data(self, topic_slug, **kwargs):
        topic = get_object_or_404(Topic, slug=topic_slug)
        comments = Comment.objects.filter(topic=topic)
        comments_number = len(Comment.objects.filter(topic=topic))
        context = {'menu': menu,
                   'topic': topic,
                   'comments': comments,
                   'comm_num': comments_number}
        return context


    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(topic=self.slug_url_kwarg)
        return self.get_mixin_context(context, subject=context['topic'].subject)
    '''


class AddTopic(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddTopicForm
    template_name = 'forum/addtopic.html'
    page_title = 'Создание новой темы'
    # success_url = reverse_lazy('topic')
    # extra_context = {'menu': menu, 'title': 'Создание новой темы'}

    '''
    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user  # user - объект текущего пользователя
        return super().form_valid(form)
    '''


class AddComment(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddCommentForm
    template_name = 'forum/addcomment.html'
    page_title = 'Оставить комментарий'
    success_url = reverse_lazy('topic')
    # extra_context = {'menu': menu, 'title': 'Оставить комментарий'}


class UpdateComment(LoginRequiredMixin, DataMixin, UpdateView):
    form_class = AddCommentForm
    template_name = 'forum/addcomment.html'
    page_title = 'Редактировать комментарий'
    success_url = reverse_lazy('topic')
    # extra_context = {'menu': menu, 'title': 'Редактировать комментарий'}


class UserProfile(DetailView):
    model = Profile
    template_name = "profile.html"


class CreateUserProfile(CreateView):
    pass


class UpdateUserProfile(UpdateView):
    pass


class DeleteUserProfile(DeleteView):
    pass


