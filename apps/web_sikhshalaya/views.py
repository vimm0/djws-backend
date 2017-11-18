from django.views.generic import ListView

from taggit.models import Tag

from apps.posts.models import Post
from apps.comments.models import Comment


class AboutList(ListView):
    model = Post
    template_name = "office_policy/about.html"


class PolicyList(ListView):
    model = Post
    template_name = "office_policy/policy.html"


class TermList(ListView):
    model = Post
    template_name = "office_policy/terms.html"


class SitemapList(ListView):
    model = Post
    template_name = "official/sitemap.html"


class ResourceList(ListView):
    model = Post
    template_name = "official/resource.html"


class ContactList(ListView):
    model = Post
    template_name = "official/contact.html"
