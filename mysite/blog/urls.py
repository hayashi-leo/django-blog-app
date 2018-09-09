# Lin,Leo - this file was manually created

from django.conf.urls import url
from . import views as blog_views

urlpatterns = [

    # django allows us the option of naming our views in case we need to reference
    # them in our code or templates.  for example
    # {% url 'post_list' %} # refers to blog_views.post_list

    url(r'^$', blog_views.post_list, name='post_list'),
    # this url approach to extract the primary key is deprecated in django 2.x
    url(r'^post/(?P<pk>\d+)/$', blog_views.post_detail, name='post_detail'),
]

