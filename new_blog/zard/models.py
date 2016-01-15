from django.db import models
from django.core.urlresolvers import reverse
class Author(models.Model):

    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return u'%s' %(self.name)


class Tag(models.Model):

    name = models.CharField(max_length=20,blank=True)
    creat_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' %(self.name)


class Classification(models.Model):

    name = models.CharField(max_length=25)

    def __unicode__(self):
        return u'%s' %(self.name)

class Article(models.Model):

    caption = models.CharField(max_length=50)
    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag,blank=True)
    classification = models.ForeignKey(Classification)
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' %(self.caption)
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id':self.id})
        return "http://127.0.0.1:8000%s" % path

class Site(models.Model):
    #id = models.AutoField()
    name = models.CharField(max_length=100)
    longitude = models.FloatField()
    lattitue = models.FloatField()
    picSrc = models.CharField(max_length=999999)
    description = models.TextField()
    author = models.ForeignKey(Author)
    caption = models.ForeignKey(Article) #one article--> many sites


class Music(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=1000)
    address = models.CharField(max_length=9999)
    album = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
