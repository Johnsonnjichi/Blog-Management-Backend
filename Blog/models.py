from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # author = models.CharField(max_length=50)

    def __str__(self):
        # return f'{self.title} - {self.author}'
        return self.title + '|' + self.author.username
        # return self.title + '|' + str(self.author)

