try:
    from urllib import quote_plus #python 2
except:
    pass

try:
    from urllib.parse import quote_plus #python 3
except: 
    pass

from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from taggit.models import Tag


from blog.apps.comments.forms import CommentForm
from blog.apps.comments.models import Comment
from .forms import PostForm
from .models import Post

# Admin stuff to workout with post manipulation
def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
		
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		# message success
		messages.success(request, "Successfully Created")

		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "admin/create_post.html", context)

def post_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')

		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "admin/create_post.html", context)

def post_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("posts:list")

# users and visitors main file
def post_list(request):
	"""
    Displays top posts.
    """
	today = timezone.now().date()
	t = Tag.objects.all().order_by('-id')[:4]

	queryset_list = Post.objects.active() #.order_by("-timestamp")
	recent_post = Post.objects.all().order_by('-id')[:3]#3 top list from descending order to time
	recent_comment = Comment.objects.all().order_by('-id')[:3]#3 top list from descending order to time
	# print(recent_comment);
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Post.objects.all()
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
				Q(title__icontains=query)|
				Q(content__icontains=query)|
				Q(user__first_name__icontains=query) |
				Q(user__last_name__icontains=query)
				).distinct()
	paginator = Paginator(queryset_list, 8) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
		"object_list": queryset, 
		"title": "Top Posts",#name in the title section in list
		"page_request_var": page_request_var,
		"recent_post": recent_post,
		"recent_comment":recent_comment,
		"today": today,
		"t":t

	}
	#authentication
	if not request.user.is_authenticated():
		return render(request, "user/post_list.html", context)
	else:
		return render(request, "user/user_post_list.html", context)

def post_detail(request, slug=None):
	"""
    Displays details of Post.
    """
    #taggit
	# tag = Post.objects.filter(
	#     tags__name__in=list(self.objects.tags.values_list('name', flat=True))
	# ).exclude(id=self.object.id)
	# tag = Post..filter(pk=pk)
	# tag_names = [tag.name for tag in Tag.objects.all()]
	# print(tag_names)
	# import pdb; pdb.set_trace()
	instance = get_object_or_404(Post, slug=slug)
	recent_post = Post.objects.all().order_by('-id')[:3]#3 top list from descending order to time
	recent_comment = Comment.objects.all().order_by('-id')[:3]#3 top list from descending order to time
	t = Tag.objects.all().order_by('-id')[:4]#for sidbar top tag
	# print(t)
	tag = instance.tags.all()
	num_tags = tag.count()
	print(tag.count())
	# tag = instance
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.content)

	initial_data = {
			"content_type": instance.get_content_type,
			"object_id": instance.id
	}
	form = CommentForm(request.POST or None, initial=initial_data)
	if form.is_valid() and request.user.is_authenticated():
		c_type = form.cleaned_data.get("content_type")
		content_type = ContentType.objects.get(model=c_type)
		obj_id = form.cleaned_data.get('object_id')
		content_data = form.cleaned_data.get("content")
		parent_obj = None
		try:
			parent_id = int(request.POST.get("parent_id"))
		except:
			parent_id = None

		if parent_id:
			parent_qs = Comment.objects.filter(id=parent_id)
			if parent_qs.exists() and parent_qs.count() == 1:
				parent_obj = parent_qs.first()


		new_comment, created = Comment.objects.get_or_create(
							user = request.user,
							content_type= content_type,
							object_id = obj_id,
							content = content_data,
							parent = parent_obj,
						)
		return HttpResponseRedirect(new_comment.content_object.get_absolute_url())


	comments = instance.comments
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
		"comments": comments,
		"comment_form":form,
		"tag":tag,
		"num_tags":num_tags,
		"recent_post":recent_post,
		"recent_comment":recent_comment,
		"t":t

	}
	#authentication
	if not request.user.is_authenticated():
		return render(request, "user/post_detail.html", context)
	else:
		return render(request, "user/user_post_detail.html", context)