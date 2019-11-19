from django.shortcuts import render
from twitterclone.twitteruser.models import TwitterUser
from twitterclone.tweet.models import Tweet


def viewprofile(request, id):
    html = 'userprofile.html'
    user = TwitterUser.objects.filter(id=id).first()
    data = Tweet.objects.filter(user=user)
    return render(request, html, {'data': data})


def followuser(request, id):
    pass
