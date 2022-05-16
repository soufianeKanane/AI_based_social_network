from post.views import *
from django.urls import path
urlpatterns = [
    path('post',postDetails),
    path('getAllPosts',getAllPosts)
]