# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from blog.managers import LikeDislikeManager


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("title"), null=False, blank=False, unique=True)
    text = models.TextField(verbose_name=_("message"), null=False, blank=False)

    post_date = models.DateTimeField(auto_now_add=True, verbose_name=_("post date"))
    # modified = models.DateTimeField(null=True, verbose_name=_("modified"))
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (DISLIKE, 'Dislike'),
        (LIKE, 'Like')
    )

    vote = models.SmallIntegerField(verbose_name=_("vote"), choices=VOTES)
    owner = models.ForeignKey(User, verbose_name=_("owner"))
    voted_post = models.ForeignKey(Post, related_name='voted_post')

    objects = LikeDislikeManager()