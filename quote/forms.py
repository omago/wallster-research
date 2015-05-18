#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Quote as Model


class QuoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuoteForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Model