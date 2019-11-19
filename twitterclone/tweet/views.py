from django.shortcuts import render, HttpResponseRedirect, reverse
from twitterclone.tweet.models import Tweet
from twitterclone.tweet.forms import MakeTweet


def viewmainpage(request):
    html = 'index.html'
    data = Tweet.objects.all().order_by('-post_time')
    return render(request, html, {'data': data})


def maketweet(request):
    html = 'tweet_form.html'
    if request.method == 'POST':
        form = MakeTweet(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(
                user=request.user,
                message=data['message']
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = MakeTweet()
    return render(request, html, {'form': form})


def viewtweet(request, id):
    html = 'view_tweet.html'
    data = Tweet.objects.filter(id=id)
    return render(request, html, {'data': data})


def liketweet(request, id):
    pass


def unliketweet(request, id):
    pass


# stretch goal
def edittweet(request, id):
    pass
