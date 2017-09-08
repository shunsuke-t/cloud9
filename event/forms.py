# coding: utf-8
from django import forms

class CreateForm(forms.Form):
    name = forms.CharField(max_length=100)
    time = forms.DateField("イベント名")
    location = forms.CharField()
    fee = forms.CharField()
    quota = forms.DecimalField(max_digits=3, decimal_places=0)

class CreateUserForm(forms.Form):
    name = forms.CharField(max_length=100)
