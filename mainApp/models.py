from django.db import models

from datetime import date


class Post(models.Model):
    date = models.DateField(default=date.today)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='mainApp/posts_img', blank=True, null=True)

    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
