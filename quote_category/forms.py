#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import QuoteCategory as Model


class QuoteCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuoteCategoryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Model