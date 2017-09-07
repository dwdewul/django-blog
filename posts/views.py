from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
# Create your views here.


def posts_home(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/post-detail.html', {'post': post})


def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.save()
        messages.success(request, "Post successfully updated!")
        return redirect(post.get_absolute_url())
    return render(request, 'posts/post-create.html', {'post': post,
                                                      'form': form})


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.save()
        messages.success(request, "Post successfully created!")
        return redirect(new_post.get_absolute_url())
    return render(request, 'posts/post-create.html', {'form': form})


def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    messages.success(request, "Post deleted")
    return redirect('posts:posts_home')
