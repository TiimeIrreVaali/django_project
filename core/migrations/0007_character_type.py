# Generated by Django 5.0.4 on 2024-05-26 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_episode_alter_news_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='type',
            field=models.CharField(choices=[('human', 'человек'), ('god', 'божество'), ('youkai', 'ёкай')], default='youkai', max_length=10, verbose_name='Тип'),
        ),
    ]
