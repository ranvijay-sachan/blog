# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("title"), null=False, blank=False, unique=True)
    text = models.TextField(verbose_name=_("message"), null=False, blank=False)

    post_date = models.DateTimeField(auto_now_add=True, verbose_name=_("post date"))
    # modified = models.DateTimeField(null=True, verbose_name=_("modified"))
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)


