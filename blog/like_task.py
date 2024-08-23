from django.shortcuts import get_object_or_404
from celery import shared_task
from django.contrib.auth.models import User
from .models import BlogPost


@shared_task
def create_task(post_id,user_id):
    post = get_object_or_404(BlogPost, id=post_id)
    user = get_object_or_404(User, id=user_id)
    print(f"Post: {post}, User: {user}")  # Debugging line
    if post.likes.filter(id=user.id).exists():
        post.likes.remove(user)
    else:
        post.likes.add(user)
