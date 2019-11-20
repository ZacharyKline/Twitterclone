from django.shortcuts import render
from twitterclone.twitteruser.models import TwitterUser
# from twitterclone.tweet.models import Tweet
from twitterclone.notification.models import Notifications


def notificationpage(request, id):
    html = 'notification/notify.html'
    twitteruser = TwitterUser.objects.filter(id=id).first()
    data = Notifications.objects.filter(user=twitteruser)
    for item in data:
        item.delete()
    return render(request, html, {'data': data})
