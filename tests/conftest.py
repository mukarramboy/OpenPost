import pytest
import json
from django.contrib.auth.models import User
from posts.models import Post, Comment

@pytest.fixture
def user(db):
    return User.objects.create_user(username="testuser", password="password")

@pytest.fixture
def post(user):
    """Фикстура для создания поста с QuillField"""
    content = json.dumps({
        "delta": [{"insert": "Hello world"}],
        "html": "<p>Hello world</p>"
    })
    return Post.objects.create(title="Test Post", content=content, author=user)

@pytest.fixture
def comment(user, post):
    """Фикстура для создания комментария к посту"""
    return Comment.objects.create(post=post, user=user, content="Nice post!")
