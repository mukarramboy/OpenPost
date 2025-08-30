# tests/comments/test_models.py
def test_comment_creation(comment):
    assert comment.content == "Nice post!"
    assert comment.post.title == "Test Post"
    assert comment.user.username == "testuser"
