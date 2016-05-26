# -*- coding: utf-8 -*-
from django import forms

class PicForm(forms.Form):
    picform = forms.FileField(
            label = 'Select a file',
            help_text = 'max 42 MegaBytes'
    )


