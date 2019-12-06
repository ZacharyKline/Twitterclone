from django.shortcuts import render, HttpResponseRedirect, reverse
from twitterclone.tweet.models import Tweet
from twitterclone.notification.models import Notifications
from twitterclone.twitteruser.models import TwitterUser
from twitterclone.tweet.forms import MakeTweet
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
import re


@method_decorator(login_required, name='dispatch')
class ViewMainPage(View):
    def get(self, request):
        html = 'tweet/index.html'
        notif = Notifications.objects.filter(
            user=request.user.twitteruser).count()
        follow = list(request.user.twitteruser.follow.all())
        tweets = []
        for followee in follow:
            tweets += Tweet.objects.filter(user=followee)
        tweets = sorted(
            tweets, key=lambda tweet: tweet.post_time, reverse=True)
        return render(request, html, {
            'tweets': tweets, 'notif': notif})


@login_required
def maketweet(request):
    html = 'tweet/tweet_form.html'
    if request.method == 'POST':
        form = MakeTweet(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_tweet = Tweet.objects.create(
                user=request.user.twitteruser,
                message=data['message']
            )
            reggie = re.findall(r'@(\w+)', data['message'])
            if reggie:
                for item in reggie:
                    try:
                        user_check = TwitterUser.objects.get(username=item)
                    except TwitterUser.DoesNotExist:
                        user_check = None
                    if user_check:
                        Notifications.objects.create(
                            user=user_check,
                            tweet=new_tweet
                        )
            return HttpResponseRedirect(reverse('homepage'))

    form = MakeTweet()
    return render(request, html, {'form': form})


class ViewTweet(View):
    def get(self, request, id):
        html = 'tweet/view_tweet.html'
        data = Tweet.objects.filter(id=id)
        return render(request, html, {'data': data})


# stretch goal
def edittweet(request, id):
    pass
