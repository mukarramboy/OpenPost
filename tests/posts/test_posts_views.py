# tests/posts/test_views.py
import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_post_list_view(client, post):
    url = reverse("post_list")
    response = client.get(url)
    assert response.status_code == 200
    assert "Test Post" in response.content.decode()

@pytest.mark.django_db
def test_post_detail_view(client, post):
    url = reverse("post_detail", args=[post.id])
    response = client.get(url)
    assert response.status_code == 200
    assert "Hello world" in response.content.decode()
