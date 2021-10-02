from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Profile(models.Model):
    username = models.CharField(max_length=25, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField()
    profile_pic = models.TextField()

    def __str__(self):
        return self.username


class Post(models.Model):
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='posts')
    post_pic = models.TextField()
    caption = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.caption


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comment')
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.post
