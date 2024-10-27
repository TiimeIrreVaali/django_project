# Generated by Django 5.1.1 on 2024-10-23 08:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_alter_topic_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='forum.topic', verbose_name='Тема'),
        ),
    ]