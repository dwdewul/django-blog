from django.shortcuts import (render, HttpResponse,
                              get_object_or_404, redirect, Http404)
from urllib.parse import quote_plus
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.


def posts_home(request):
    posts_list = Post.objects.all().order_by('-timestamp')
    paginator = Paginator(posts_list, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'posts/index.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    share_string = quote_plus(post.content)
    return render(request, 'posts/post-detail.html', {'post': post,
                                                      'share_string': share_string})


def post_update(request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.save()
        messages.success(request, "Post successfully updated!")
        return redirect(post.get_absolute_url())
    return render(request, 'posts/post-create.html', {'post': post,
                                                      'form': form})


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.user = request.user
        new_post.save()
        messages.success(request, "Post successfully created!")
        return redirect(new_post.get_absolute_url())
    return render(request, 'posts/post-create.html', {'form': form})


def post_delete(request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, "Post deleted")
    return redirect('posts:posts_home')
