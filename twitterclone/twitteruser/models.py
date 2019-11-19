from django.db import models
from django.contrib.auth.models import User


class TwitterUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    bio = models.CharField(max_length=200, blank=True, null=True)
    follow = models.ManyToManyField('self')

    def __str__(self):
        return f'{self.username}'
