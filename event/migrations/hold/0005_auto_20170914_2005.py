# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-14 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20170913_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='members',
            field=models.ManyToManyField(to='event.Person'),
        ),
    ]