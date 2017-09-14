# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-14 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_remove_event_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='members',
            field=models.ManyToManyField(to='event.Person'),
        ),
    ]