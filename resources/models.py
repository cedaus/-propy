from __future__ import unicode_literals
from django.db import models

class ResourceCategory(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=75, unique=True)

    def __unicode__(self):
        return unicode(self.name)

class ResourceTag(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return unicode(self.name)

class ResourcePublisher(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return unicode(self.name)

class Resource(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    edited = models.DateTimeField(auto_now_add=True, editable=True)
    title = models.CharField(max_length=100)
    comment = models.TextField()
    category = models.ForeignKey(ResourceCategory)
    tags = models.ManyToManyField(ResourceTag)
    publisher = models.ForeignKey(ResourcePublisher)
    link = models.TextField()

    def __unicode__(self):
        return unicode(self.title)

class Collection(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now_add=True, editable=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(ResourceCategory)
    resources = models.ManyToManyField(Resource, through='ResourceCollectionAssociation', through_fields=('collection','resource'))

    def __unicode__(self):
        return unicode(self.title)

class ResourceCollectionAssociation(models.Model):
    collection = models.ForeignKey(Collection)
    resource = models.ForeignKey(Resource)

    def __unicode__(self):
        return self.collection.__unicode__() + " : " + self.resource.__unicode__()
