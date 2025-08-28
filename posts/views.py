from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.

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
