from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts', kwargs={'post_slug': self.slug})


    class Meta:
        ordering = ['-time_create']
        indexes = [models.Index(fields=['-time_create'])]


class Character(models.Model):

    FACTION_CHOICES = (
        ('outers', 'Внешний мир'),
        ('resistance', 'Сопротивление'),
        ('neutrals', 'Нейтральные персонажи'),
        ('domination', 'Волшебное Превосходство'),
        ('moon', 'Луна'),
    )

    TYPE_CHOICES = (
        ('human', 'человек'),
        ('god', 'божество'),
        ('youkai', 'ёкай'),
    )

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, blank=True, db_index=True, default='')
    type = models.CharField('Тип', max_length=10, choices=TYPE_CHOICES, default='youkai')
    faction = models.CharField('Фракция', max_length=100, choices=FACTION_CHOICES, default='neutrals')
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="static/core/images/%Y/%m/%d/", blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('chars', kwargs={'char_slug': self.slug})

    class Meta:
        ordering = ['time_create']
        indexes = [models.Index(fields=['time_create'])]


class Episode(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.title
