# posts/models.py
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

class Post(models.Model):
    name = models.CharField(max_length=224, null=False, blank=False)
    content = models.TextField(max_length=254, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Species(models.Model):
    name = models.CharField(max_length=100)
    classification = models.CharField(max_length=100)
    language = models.CharField(max_length=100)

class Person(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.CharField(max_length=10)
    eye_color = models.CharField(max_length=10)
    species = models.ForeignKey(Species, on_delete=models.DO_NOTHING)

class Car(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.content
