#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Quoter as Model


class QuoterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuoterForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Model