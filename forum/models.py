from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from autoslug import AutoSlugField


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=32, default='')
    name = models.CharField(max_length=32, default='')
    email = models.EmailField(max_length=254, blank=True, unique=True)
    bio = models.TextField(max_length=500, default="Write a couple of words about yourself")
    avatar = models.ImageField(default=None, blank=True, max_length=255)
    status = models.CharField(max_length=25, blank=True, default='')
    slug = models.SlugField()

    def __str__(self):
        return f'{self.user} profile'

    def get_absolute_url(self):
        return reverse('user_profile', kwargs={'profile_slug': self.slug})

    def save(self, *args, **kwargs):
        super(Profile, self).save()
        if not self.id:
            self.slug += '-' + str(self.id)
            super(Profile, self).save(*args, **kwargs)


class Subforum(models.Model):
    news = 'News'
    chars = 'Characters'
    eps = 'Episodes'
    refs = 'References'
    prod = 'Production'
    bugs = 'bugs'

    THEME_CHOICES = (
        (news, "News"),
        (chars, "Characters"),
        (eps, "Episodes"),
        (refs, "References"),
        (prod, "Production"),
        (bugs, "Bugs"),
    )

    title = models.CharField(verbose_name='Название', max_length=32, choices=THEME_CHOICES, default=1)
    slug = AutoSlugField(default='News', populate_from='title')

    class Meta:
        ordering = ['title']
        verbose_name = 'Разделы форума'
        verbose_name_plural = 'Разделы форума'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forum.subforum', kwargs={'name': self.title})


class Topic(models.Model):
    subject = models.CharField(verbose_name='Заголовок', max_length=255, unique=True)
    slug = models.SlugField(blank=True, unique=True)
    subforum = models.ForeignKey('Subforum',
                                 verbose_name='Раздел',
                                 on_delete=models.CASCADE,
                                 related_name='subforum')
    creator = models.ForeignKey('User',
                                verbose_name='Создатель темы',
                                on_delete=models.SET('deleted'),
                                related_name='creator')
    created = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']
        verbose_name = 'Обсуждения'
        verbose_name_plural = 'Обсуждения'

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('topic', kwargs={'topic_slug': self.slug})

    def save(self, *args, **kwargs):
        super(Topic, self).save()
        if not self.id:
            self.slug += '-' + str(self.id)
            super(Topic, self).save(*args, **kwargs)


class Comment(models.Model):
    topic = models.ForeignKey('Topic',
                              verbose_name='Тема',
                              on_delete=models.CASCADE,
                              related_name='topic')
    author = models.ForeignKey('User',
                               verbose_name='Комментатор',
                               on_delete=models.SET('deleted'),
                               related_name='author')
    content = models.TextField(verbose_name='Текст', max_length=2000)
    created = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    slug = models.SlugField(blank=True, unique=True)

    class Meta:
        ordering = ['created']
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Post of {self.topic.subject} is posted by {self.author.username}.'

    def get_absolute_url(self):
        return reverse('comment', kwargs={'comment_slug': self.slug})

    def save(self, *args, **kwargs):
        super(Comment, self).save()
        if not self.id:
            self.slug += '-' + str(self.id)
            super(Comment, self).save(*args, **kwargs)
