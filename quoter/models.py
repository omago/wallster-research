#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


class Quoter(models.Model):
    name = models.CharField(max_length=128, verbose_name="Naziv")
    link = models.CharField(max_length=1024, verbose_name="link", blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-pk']
        db_table = "quoter"