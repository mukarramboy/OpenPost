from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Добро пожаловать, {user.username}!")
            return redirect("post_list")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("post_list")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("post_list")
    else:
        form = UserCreationForm()
    return render(request, "users/signup.html", {"form": form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})



@login_required
def add_comment(request, pk):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=pk)
        content = request.POST.get("content")
        parent_id = request.POST.get("parent")

        parent = None
        if parent_id:
            parent = Comment.objects.get(id=parent_id)

        Comment.objects.create(
            post=post,
            user=request.user,
            content=content,
            parent=parent
        )
    return redirect("post_detail", pk=pk)


@login_required
def like_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user in comment.likes.all():
        comment.likes.remove(request.user)  # если уже лайкнул → убираем
    else:
        comment.likes.add(request.user)  # иначе добавляем
    return redirect("post_detail", pk=comment.post.pk)
