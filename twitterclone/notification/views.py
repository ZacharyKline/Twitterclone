from django.shortcuts import render
from twitterclone.twitteruser.models import TwitterUser
from twitterclone.notification.models import Notifications
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View


@method_decorator(login_required, name='dispatch')
class NotificationPage(View):
    def get(self, request, id):
        html = 'notification/notify.html'
        twitteruser = TwitterUser.objects.filter(id=id).first()
        data = Notifications.objects.filter(user=twitteruser)
        for item in data:
            item.delete()
        return render(request, html, {'data': data})
