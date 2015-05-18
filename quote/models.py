#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from quoter.models import Quoter
from quote_category.models import QuoteCategory


class Quote(models.Model):
    quoter = models.ForeignKey(Quoter, verbose_name="Citator")
    quote_category = models.ManyToManyField(QuoteCategory, verbose_name="Kategorija")
    quote = models.TextField(verbose_name="Citat")

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-pk']
        db_table = "quote"