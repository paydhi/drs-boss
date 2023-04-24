from django.shortcuts import render
from rest_framework import generics
from posts.models import Post
from posts.serializers import PostSerializer

# Create your views here.

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer