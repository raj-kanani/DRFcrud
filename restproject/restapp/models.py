from django.db import models
from django.db.models.fields import SlugField, EmailField, IntegerField, CharField, URLField
from django.forms.fields import RegexField, FilePathField


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name
