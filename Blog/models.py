from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title[:10]}.... by {self.author}'
    