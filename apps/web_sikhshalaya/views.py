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
    queryset = Post.objects.all()
    template_name = "official/sitemap.html"

    def get_context_data(self, **kwargs):
        context = super(SitemapList, self).get_context_data(**kwargs)
        context['recent_comment'] = Comment.objects.all().order_by('-id')[:3]
        context['top_tag'] = Tag.objects.all().order_by('-id')[:4]
        return context


class ResourceList(ListView):
    model = Post
    queryset = Post.objects.all().order_by('-id')[:3]
    template_name = "official/resource.html"


class ContactList(ListView):
    model = Post
    queryset = Post.objects.all().order_by('-id')[:3]
    template_name = "official/contact.html"
