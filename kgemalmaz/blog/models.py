from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class Post(models.Model):
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    original_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Comment by " + self.author.__str__() + " under " + self.original_post.__str__()