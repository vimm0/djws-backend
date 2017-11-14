from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

    )
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from .tokens import account_activation_token
from .forms import UserLoginForm, UserRegisterForm

def login_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")
    return render(request, "user/form.html", {"form":form, "title": title})


def register_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        current_site = get_current_site(request)
        message = render_to_string('user/activate_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        mail_subject = 'Activate your blog account.'
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()
        import pdb
        pdb.set_trace()
        return HttpResponse('Please confirm your email address to complete the registration')
        # new_user = authenticate(username=user.username, password=password)
        # login(request, new_user)
        # if next:
        #     return redirect(next)
        # return redirect("/")
    else:
        form = UserRegisterForm()

    context = {
        "form": form,
        "title": title
    }
    return render(request, "user/signup.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")

def user_detail_view(request):
    return render(request, "user/user_profile.html")

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')