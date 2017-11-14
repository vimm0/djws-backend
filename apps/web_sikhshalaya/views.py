from django.shortcuts import render, get_object_or_404

from apps.posts.models import *
from taggit.models import Tag


# Create your views here.
# def about_office_view(request):
# instance = get_object_or_404(Post, slug=slug)
# return render(request, "office_policy/about_office.html" )

def about_view(request):
    # instance = get_object_or_404(Post, slug=slug)
    return render(request, "office_policy/about.html")


def policy_view(request):
    return render(request, "office_policy/policy.html")


def terms_view(request):
    return render(request, "office_policy/terms.html")


def sitemap_view(request):
    instance = Post.objects.all()
    recent_post = Post.objects.all().order_by('-id')[:3]  # 3 top list from descending order to time
    recent_comment = Comment.objects.all().order_by('-id')[:3]  # 3 top list from descending order to time
    top_tag = Tag.objects.all().order_by('-id')[:4]  # for sidbar top tag

    context = {
        "recent_post": recent_post,
        "recent_comment": recent_comment,
        "instance": instance,
        "top_tag": top_tag,
    }
    return render(request, "official/sitemap.html", context)


def resource_view(request):
    # app_url = request.path
    recent_post = Post.objects.all().order_by('-id')[:3]  # 3 top list from descending order to time
    recent_comment = Comment.objects.all().order_by('-id')[:3]  # 3 top list from descending order to time
    top_tag = Tag.objects.all().order_by('-id')[:4]  # for sidbar top tag
    context = {
        "recent_post": recent_post,
        "recent_comment": recent_comment,
        "top_tag": top_tag,
    }
    return render(request, "official/resource.html", context)


def contact_view(request):
    # app_url = request.path
    recent_post = Post.objects.all().order_by('-id')[:3]  # 3 top list from descending order to time
    recent_comment = Comment.objects.all().order_by('-id')[:3]  # 3 top list from descending order to time
    top_tag = Tag.objects.all().order_by('-id')[:4]  # for sidbar top tag
    context = {
        "recent_post": recent_post,
        "recent_comment": recent_comment,
        "top_tag": top_tag,
    }
    return render(request, "official/contact.html", context)
