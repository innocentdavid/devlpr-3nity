from django.db import models
from django.contrib.auth.models import User

import json
from json import JSONEncoder

# Create your models here.

class Visitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    fname = models.CharField(max_length=200)
    # lname = models.CharField(max_length=200)

    def __str__(self):
        return self.fname

class Moderator(models.Model):
    user = models.CharField(max_length=200, default="AnonymousUser")
    totalLikes = models.CharField(max_length=200, default=0)
    totalPosts = models.CharField(max_length=200, default=0)
    totalFollowers = models.CharField(max_length=200, default=0)
    facebook = models.CharField(max_length=200, default='#')
    instagram = models.CharField(max_length=200, default='#')
    twitter = models.CharField(max_length=200, default='#')
    linkedIn = models.CharField(max_length=200, default='#')
    whatsapp = models.CharField(max_length=200, default='tel:+2348 112 659 304')

    def __str__(self):
        return self.user

class Post(models.Model):
    author = models.ForeignKey(Moderator, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    videoLink = models.CharField(max_length=200)
    rating = models.CharField(max_length=200, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    visitor = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    timestamp = models.CharField(max_length=200)

    def __str__(self):
        return self.visitor

