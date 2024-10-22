from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

from .consts import *


'''
class User(AbstractUser):
    class Meta:
        app_label = 'forum'
'''


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=32, default='')
    name = models.CharField(max_length=32, default='')
    email = models.EmailField(max_length=254, blank=True, unique=True)
    bio = models.TextField(max_length=500, default="Write a couple of words about yourself")
    avatar = models.ImageField(default=None, blank=True, max_length=255)
    status = models.CharField(max_length=25, blank=True, default='')
    slug = models.SlugField()
    age = models.IntegerField(verbose_name='Возраст', null=True, blank=True)
    gender = models.CharField(verbose_name='Пол', max_length=32, choices=Genders.GENDER_CHOICES, default="H", blank=True)
    reputation = models.IntegerField(verbose_name='Репутация', default=0)

    def __str__(self):
        return f'{self.user} profile'

    def get_absolute_url(self):
        return reverse('forum:user_profile', kwargs={'profile_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.user.username)
            return super(Profile, self).save(*args, **kwargs)


class Subforum(models.Model):
    title = models.CharField(verbose_name='Название', max_length=32, choices=Theme.THEME_CHOICES, default=1)
    slug = models.SlugField(default='News')
    objects = models.Manager()

    class Meta:
        ordering = ['title']
        verbose_name = 'Разделы форума'
        verbose_name_plural = 'Разделы форума'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
            return super(Subforum, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('forum:subforum', kwargs={'subforum_slug': self.slug})


class Topic(models.Model):
    subject = models.CharField(verbose_name='Заголовок', max_length=255, unique=True)
    first_comment = models.TextField(verbose_name='Сообщение', max_length=2000, default='')
    slug = models.SlugField(default='', unique=True, max_length=25, editable=False)
    subforum = models.ForeignKey('Subforum',
                                 verbose_name='Раздел',
                                 on_delete=models.CASCADE,
                                 related_name='subforum')
    creator = models.ForeignKey(User,
                                verbose_name='Создатель темы',
                                on_delete=models.SET('deleted'),
                                related_name='creator')
    created = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    objects = models.Manager()

    class Meta:
        ordering = ['id']
        verbose_name = 'Обсуждения'
        verbose_name_plural = 'Обсуждения'

    def __str__(self):
        return self.subject

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = f'topic-{slugify(self.subject)}'[0:25]
            return super(Topic, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('forum:topic', kwargs={'topic_slug': self.slug})


class Comment(models.Model):
    topic = models.ForeignKey('Topic',
                              verbose_name='Тема',
                              on_delete=models.CASCADE,
                              related_name='topic')
    author = models.ForeignKey(User,
                               verbose_name='Комментатор',
                               on_delete=models.SET('deleted'),
                               related_name='author')
    content = models.TextField(verbose_name='Текст', max_length=2000)
    created = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    objects = models.Manager()

    class Meta:
        ordering = ['created']
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Post of {self.topic.subject} is posted by {self.author.username}.'
