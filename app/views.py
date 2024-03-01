from django.shortcuts import render

from .models import Post

from django.shortcuts import render, redirect

from .forms import PostForm

from django.shortcuts import redirect

from .forms import UserRegistrationForm

from .forms import UserLoginForm

from django.contrib.auth import logout

from .forms import UserPasswordChangeForm

from .forms import UserPasswordResetForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})


def post_update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_update.html', {'form': form})


def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('post_list')


def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user_registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'user_login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


def user_password_change(request):
    if request.method == 'POST':
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserPasswordChangeForm(request.user)
    return render(request, 'user_password_change.html', {'form': form})


def user_password_reset(request):
    if request.method == 'POST':
        form = UserPasswordResetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserPasswordResetForm()
    return render(request, 'user_password_reset.html', {'form': form})