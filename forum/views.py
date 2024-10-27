from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from rest_framework import viewsets

from core.views import menu
from .filters import TopicFilter
from .forms import AddTopicForm, AddCommentForm
from .models import Subforum, Topic, Comment, Profile
from .serializers import *
from .utils import DataMixin


class TopicAPI(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class CommentAPI(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class SubForumListView(ListView):
    model = Subforum
    context_object_name = 'subforum_list'
    template_name = "forum/forum.html"

    def get_context_data(self, **kwargs):
        subforums = Subforum.objects.all()
        context = {'subforums': subforums}
        return context


class TopicListView(FilterView):
    model = Topic
    template_name = "forum/subforum.html"
    slug_url_kwarg = 'subforum_slug'
    context_object_name = 'topics'
    filterset_class = TopicFilter

    def get_queryset(self):
        qs = self.model.objects.all()
        if self.kwargs.get('subforum_slug'):
            qs = qs.filter(subforum__slug=self.kwargs['subforum_slug'])
        return qs


class ShowTopic(DetailView):
    model = Topic
    template_name = "forum/topic.html"
    slug_url_kwarg = 'topic_slug'
    context_object_name = 'topic'

    def get_context_data(self, **kwargs):
        topic = get_object_or_404(Topic, slug=self.kwargs['topic_slug'])
        comments = Comment.objects.filter(topic=topic)
        comments_number = len(Comment.objects.filter(topic__id=topic.id))
        context = {'menu': menu,
                   'topic': topic,
                   'comments': comments,
                   'comm_num': comments_number}
        return context


class AddTopic(DataMixin, CreateView):
    form_class = AddTopicForm
    template_name = 'forum/addtopic.html'
    page_title = 'Создание новой темы'

    def get_success_url(self):
        return reverse('forum:topic', kwargs={
            'subforum_slug': self.kwargs['subforum_slug']})

    def form_valid(self, form):
        subforum = Subforum.objects.get(slug=self.kwargs['subforum_slug'])
        form.instance.creator = self.request.user
        form.instance.subforum = subforum
        return super(AddTopic, self).form_valid(form)


class AddComment(LoginRequiredMixin, DataMixin, CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'forum/addcomment.html'
    page_title = 'Оставить комментарий'

    def get_success_url(self):
        return reverse('forum:topic', kwargs={
            'subforum_slug': self.kwargs['subforum_slug'],
            'topic_slug': self.kwargs['topic_slug']})

    def form_valid(self, form):
        topic = Topic.objects.get(slug=self.kwargs['topic_slug'])
        form.instance.author = self.request.user
        form.instance.topic = topic
        return super(AddComment, self).form_valid(form)


class UpdateComment(LoginRequiredMixin, DataMixin, UpdateView):
    model = Comment
    form_class = AddCommentForm
    context_object_name = 'comment'
    template_name = 'forum/editcomment.html'
    page_title = 'Редактировать комментарий'

    def get_success_url(self):
        return reverse('forum:topic', kwargs={
            'subforum_slug': self.kwargs['subforum_slug'],
            'topic_slug': self.kwargs['topic_slug']
        })

    def form_valid(self, form):
        topic = Topic.objects.get(slug=self.kwargs['topic_slug'])
        comment_id = self.kwargs['pk']
        form.instance.author = self.request.user
        form.instance.topic = topic
        form.instance.id = comment_id
        return super(UpdateComment, self).form_valid(form)


class DeleteComment(LoginRequiredMixin, DataMixin, DeleteView):
    model = Comment
    context_object_name = 'comment'
    template_name = 'forum/comment_confirm_delete.html'
    page_title = "Удаление комментария"
    fields = '__all__'

    def get_success_url(self):
        return reverse('forum:topic', kwargs={
            'subforum_slug': self.kwargs['subforum_slug'],
            'topic_slug': self.kwargs['topic_slug']
        })


class UserProfile(DetailView):
    model = Profile
    template_name = "profile.html"
