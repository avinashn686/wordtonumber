# _*_ coding: utf-8 _*_
from __future__ import unicode_literals

from django import forms


class Home_form(forms.Form):
    inputs = forms.CharField(max_length=20)
    outputs = forms.CharField(max_length=200, required=False)
