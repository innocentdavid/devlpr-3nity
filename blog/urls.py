from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register_view, name="register_view"),
    path("login", views.login_view, name="login_view"),
    path("logout", views.logout_view, name="logout_view"),

    path("", views.index, name="index"),
    path("blog", views.blogHome, name="blogHome"),
    path("blog/<str:title>", views.blog, name="blog"),
    path("author/<str:author>", views.author, name="author"),
    path("comment", views.comment, name="comment"),
    path("createPost", views.createPost, name="createPost"),
]