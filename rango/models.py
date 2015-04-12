from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User)
    followers = models.ManyToManyField('self', related_name="follower")
    rating = models.IntegerField()

class TagList(models.Model):
    tag = models.CharField(max_length=128)

class Composition(models.Model):
    filename = models.CharField(max_length=192)
    tag_list = models.ManyToManyField(TagList, related_name="composition_tag")
    genre = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    album = models.CharField(max_length=256)
    owner = models.ForeignKey(Profile, related_name="composition")
    rating = models.IntegerField()

class Playlist(models.Model):
    composition_list = models.ManyToManyField(Composition, related_name="playlist")
    user = models.ForeignKey(Profile, related_name="playlist")
    info = models.CharField(max_length=1024)

class Storage(models.Model):
    address = models.CharField(max_length=256)
