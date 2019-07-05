from django.db import models


# Create your models here.
class Artist(models.Model):
    f_name = models.CharField(max_length=20, null=True)
    l_name = models.CharField(max_length=20, null=True)
    nick_name = models.CharField(max_length=20, null=True)
    avatar = models.ImageField(null=True, blank=False, upload_to='albums/%Y-%m-%d/')


class Album(models.Model):
    title = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=20, null=True)
    summary = models.TextField(null=True)
    rate = models.FloatField(null=True, default=0)
    like = models.PositiveIntegerField(null=True, default=0)
    release_date = models.DateField(null=True)
    cover = models.ImageField(null=True, blank=False, upload_to='albums/%Y-%m-%d/')


class Image(models.Model):
    title = models.CharField(max_length=20, null=True)
    Image = models.FileField(null=True, blank=False, upload_to='albums/%Y-%m-%d/')


class Tag(models.Model):
    title = models.CharField(max_length=20, null=True)
