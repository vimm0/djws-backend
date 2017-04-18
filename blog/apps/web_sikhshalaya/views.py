from django.shortcuts import render

# Create your views here.
# def about_office_view(request):
	# instance = get_object_or_404(Post, slug=slug)
	# return render(request, "office_policy/about_office.html" )

def about_view(request):
	# instance = get_object_or_404(Post, slug=slug)
	return render(request, "office_policy/about.html" )

def policy_view(request):
	return render(request, "office_policy/policy.html")

def terms_view(request):
	return render(request, "office_policy/terms.html")

def sitemap_view(request):
	# app_url = request.path
	return render(request, "official/sitemap.html")

def resource_view(request):
	# app_url = request.path
	return render(request, "official/resource.html")

def contact_view(request):
	# app_url = request.path
	return render(request, "official/contact.html")

