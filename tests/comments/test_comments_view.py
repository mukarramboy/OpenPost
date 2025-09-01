import pytest
from posts.models import Comment

from django.urls import reverse

@pytest.mark.django_db
def test_comment_creation(client, post, user):
    client.login(username=user.username, password="password")
    response = client.post(reverse("add_comment", args=[post.id]), {"content": "Test comment"})
    assert response.status_code == 302
    assert Comment.objects.count() == 1
    assert Comment.objects.first().content == "Test comment"


@pytest.mark.django_db
def test_like_comment(client, comment, user):
    client.login(username=user.username, password="password")
    response = client.post(reverse("like_comment", args=[comment.id]))
    assert response.status_code == 302
    assert comment.likes.count() == 1
    response = client.post(reverse("like_comment", args=[comment.id]))
    assert response.status_code == 302
    assert comment.likes.count() == 0
