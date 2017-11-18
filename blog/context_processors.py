from django.utils import timezone
from django.shortcuts import render
from django.views.generic import ListView

from taggit.models import Tag

from apps.posts.models import Post
from apps.comments.models import Comment


def sidebar(request):
    today = timezone.now().date()
    recent_post = Post.objects.all().order_by('-id')[:3]
    recent_comment = Comment.objects.all().order_by('-id')[:3]
    top_tag = Tag.objects.all().order_by('-id')[:4]
    context = {
        "today": today,
        "recent_post": recent_post,
        "recent_comment": recent_comment,
        "top_tag": top_tag,
    }
    return context
