from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProfileSerializer, PostSerializer
from .models import Profile, Post

# Create your views here.


class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
