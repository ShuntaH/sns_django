import os

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    pass


def image_post_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/post/<post_title>.拡張子
    filename_divided = os.path.splitext(filename)
    ext = filename_divided[1]
    filename = 'post/{0}{1}'.format(instance.title, ext)
    return filename


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField('content')
    author = models.CharField(max_length=100)
    images = models.ImageField(upload_to=image_post_directory_path)
    like = models.IntegerField('like', default=0)
    read = models.IntegerField('read', default=0)
    readtxt = models.CharField(max_length=200)
    created_at = models.DateTimeField('Created at', default=timezone.now)

    def __str__(self):
        return self.title


