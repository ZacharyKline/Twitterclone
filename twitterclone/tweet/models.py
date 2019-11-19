from django.db import models
from django.utils import timezone
from twitterclone.authentication.models import TwitterUser


class Tweet(models.Model):
    user = models.ForeignKey(TwitterUser)
    message = models.TextField(max_length=280)
    like = models.IntegerField(default=0)
    post_time = models.DateField(default=timezone.now)
