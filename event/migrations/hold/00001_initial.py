# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-14 11:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200, verbose_name=b'\xe4\xbd\x9c\xe6\x88\x90\xe8\x80\x85')),
                ('event_name', models.CharField(max_length=200, verbose_name=b'\xe3\x82\xa4\xe3\x83\x99\xe3\x83\xb3\xe3\x83\x88\xe5\x90\x8d')),
                ('event_image', models.ImageField(blank=True, upload_to=b'', verbose_name=b'\xe3\x82\xa4\xe3\x83\xa1\xe3\x83\xbc\xe3\x82\xb8\xe7\x94\xbb\xe5\x83\x8f')),
                ('event_datetime', models.DateTimeField(blank=True, null=True, verbose_name=b'\xe6\x97\xa5\xe6\x99\x82')),
                ('event_location', models.CharField(max_length=200, verbose_name=b'\xe9\x96\x8b\xe5\x82\xac\xe5\xa0\xb4\xe6\x89\x80')),
                ('num_of_members', models.CharField(max_length=200, verbose_name=b'\xe5\x8b\x9f\xe9\x9b\x86\xe4\xba\xba\xe6\x95\xb0')),
                ('dead_line', models.DateField(verbose_name=b'\xe5\x8b\x9f\xe9\x9b\x86\xe7\xb7\xa0\xe5\x88\x87\xe6\x97\xa5')),
                ('overview', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Person'),
        ),
        migrations.AddField(
            model_name='event',
            name='members',
            field=models.ManyToManyField(through='event.Membership', to='event.Person'),
        ),
    ]
