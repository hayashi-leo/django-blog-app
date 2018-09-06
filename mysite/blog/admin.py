# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Post

admin.site.register(Post) # this makes our model Post visible on the Admin Page
