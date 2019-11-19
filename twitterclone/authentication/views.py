from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from twitterclone.authentication.forms import LoginForm, UserAdd
from twitterclone.twitteruser.models import TwitterUser
# from django.contrib.auth.models import User


def loginview(request):
    html = 'login.html'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, html, {'form': form})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


def createuser(request):
    html = 'adduser.html'
    if request.method == 'POST':
        form = UserAdd(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            TwitterUser.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = UserAdd()
    return render(request, html, {'form': form})
