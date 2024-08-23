from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=50,blank=True,null=True)
    likes = models.ManyToManyField(User, related_name='blogpost_like')

    def number_of_likes(self):
        return self.likes.count()
