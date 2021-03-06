from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProfileSerializer, PostSerializer, CommentSerializer
from .models import Profile, Post, Comment

# Create your views here.


class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
