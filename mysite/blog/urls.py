# Lin,Leo - this file was manually created

from django.conf.urls import url
from . import views as blog_views

urlpatterns = [
    url(r'^$', blog_views.post_list, name='post_list'),
]