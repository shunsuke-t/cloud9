# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-12 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=models.ImageField(blank=True, upload_to=b'', verbose_name=b'\xe3\x82\xa4\xe3\x83\xa1\xe3\x83\xbc\xe3\x82\xb8\xe7\x94\xbb\xe5\x83\x8f'),
        ),
    ]