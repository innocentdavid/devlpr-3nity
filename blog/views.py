import re
from markdown2 import markdown
import json

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from .models import *
from . import util

# Create your views here.
date = datetime.now().strftime('%Y/%m/%d %I:%M:%S')

@csrf_exempt
def index(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        action = data.get('action')
        if action == 'status':
            if request.user.is_authenticated:
                return JsonResponse({"user":request.user.visitor.fname})
            user = str(request.user)
            return JsonResponse({"user":user})

    return HttpResponseRedirect(reverse("blogHome"))
    # return render(request, "blog/index.html")

def blogHome(request):
    post = Post.objects.all()
    return render(request, "blog/blog.html", {"post":post})

# singleBlog
@csrf_exempt
def blog(request, title):
    print(date)
    res = util.search(title)
    if res == None:
        return HttpResponse(f'"{title}" Entry Not Found!')

    if res == title:
        f = default_storage.open(f"entries/{res}.md")
        fr = f.read().decode("utf-8")
        entry = markdown(fr)
        post = Post.objects.filter(title=res.capitalize())
        randPost = Post.objects.all().order_by('?')[:6]
        if post:
            comments = Comment.objects.filter(post=Post.objects.filter(title=res.capitalize()).order_by('-id').first()).order_by('-id')
            return render(request, "blog/singleBlog.html", {"entry": entry, "post":post, "comments":comments, "randPost":randPost})
        else:
            return HttpResponse(f'"{title}" Post Not Found!')
    else:
        return render(request, "blog/blogSearch.html", {"entryList": res})

def author(request, author):
    return render(request, "blog/author.html", {"author":author})

@csrf_exempt
def comment(request):
    data = json.loads(request.body)
    action = data.get('action')
    postId = data.get('postId')
    visitor = data.get('visitor')
    body = data.get('body')
    if action == 'count':
        commentCount = Comment.objects.filter(post=Post.objects.get(pk=postId)).count()
        return JsonResponse({"commentCount":commentCount})
    else:
        comment = Comment(visitor=visitor, post=Post.objects.get(pk=postId), body=body, timestamp=datetime.now().strftime('%Y/%m/%d %I:%M:%S'))
        comment.save()
        return JsonResponse({"message":'ok'})

@csrf_exempt
def createPost(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            posts = Post.objects.filter(pk=data['id'])
            for post in posts:
                title = post.title
                tags = post.tags
                fVideo = post.videoLink
                res = util.search(title.lower())
                if res == None:
                    return JsonResponse({"message":f'{title} Entry Not Found!'})
                if res == title.lower():
                    f = default_storage.open(f"entries/{res}.md")
                    fr = f.read().decode("utf-8")
                    # entry = markdown(fr)
                    return JsonResponse({"title":title,"tags":tags,"fVideo":fVideo,"content":str(fr)})
        except:
            pass

        author = data['fname']
        title = data['title'].capitalize()
        tags = data['tags']
        fVideo = data['fVideo']
        content = data['content']
        
        res = util.create_entry(title, content)
        if res == "success":
            moderator, created = Moderator.objects.get_or_create(user = author)
            post, created = Post.objects.update_or_create(author=moderator,title=title,tags=tags, videoLink=fVideo)
            return JsonResponse({"message":'ok'})
        else:
            return JsonResponse({"message":res})

    posts = Post.objects.filter(author=Moderator.objects.get(user=f'{request.user.visitor.fname}'))
    context = {"posts":posts}
    return render(request, "blog/createPost.html", context)

def register_view(request):
    if request.method == 'POST':
        username = request.POST['email']
        fname = (request.POST['fname']).capitalize()
        lname = (request.POST['lname']).capitalize()
        password = request.POST['password']
        confirmation = request.POST["cpassword"]
        if password != confirmation:
            return render(request, "blog/register.html", {
                "message": "Passwords must match."
            })

        try:
            email=''
            user = User.objects.create_user(username, email, password)
            user.save()
            
        except IntegrityError:
            return render(request, "blog/register.html", {"message": "Email address already taken."})
        
        login(request, user)
        visitor = Visitor(user=request.user, fname=fname,lname=lname)
        visitor.save()
        return HttpResponseRedirect(reverse("blog"))
    return render(request, "blog/register.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login_view"))

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            try:
                if request.POST['next'] != '':
                    return HttpResponseRedirect(reverse(request.POST['next']))
            except:
                pass
            return HttpResponseRedirect(reverse("index"))
        return render(request, "blog/login.html", {"message": "Incorrect credentials or User does not exiest."})
    return render(request, "blog/login.html")