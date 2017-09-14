# coding: utf-8
from django import forms
from django.forms import ModelForm
from . import models

from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            'author', 'event_name', 'event_image', 'event_datetime', 
            'event_location', 'num_of_members', 'dead_line', 'overview'
        ]


class CreateForm(forms.Form):
    author = forms.CharField(max_length=200,label='作成者')
    event_name = forms.CharField(max_length=200)
    event_image = forms.ImageField(required=False)
    event_datetime = forms.DateTimeField(required=False)
    event_location = forms.CharField(max_length=200)
    num_of_members = forms.CharField(max_length=200)
    dead_line = forms.DateField()
    overview = forms.CharField(max_length=2000)

class CreateUserForm(forms.Form):
    name = forms.CharField(max_length=100)
    
class SelectUserForm(forms.Form):
    new_members = forms.ModelChoiceField(
        models.Person.objects,
        label='メンバー',
        empty_label='選択してください',
        to_field_name='id')