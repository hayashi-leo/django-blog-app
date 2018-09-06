# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # this is a link to another Model
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_data = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_data = timezone.now()
        self.save()

    def __str__(self):
        return self.title