# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-10 06:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0009_video_stream'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='youtube_video',
        ),
    ]