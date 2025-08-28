from django.db import models
from django.contrib.auth.models import User
from django_quill.fields import QuillField


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = QuillField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    user = models.ForeignKey(
        User,  # пользователь, вошедший через Google OAuth
        on_delete=models.CASCADE,
        related_name="comments"
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="replies"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # лайки
    likes = models.ManyToManyField(
        User,
        related_name="liked_comments",
        blank=True
    )

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.user.username}: {self.content[:30]}"

    @property
    def likes_count(self):
        return self.likes.count()

    @property
    def is_reply(self):
        return self.parent is not None
