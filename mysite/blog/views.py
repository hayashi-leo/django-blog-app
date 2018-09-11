# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts}) # passing args as dictionary to template


# post detail view
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post })

# post new view
def post_new(request):
    if request.method == 'POST':
        # if htttp POST was submitted
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # don't commit, we will do it later
            post.author = request.user
            post.published_date = timezone.now()
            post.save() # Ok, now we save it
            return redirect('post_detail', pk=post.pk)  # now navigate to post details
    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})


# post edit view
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

