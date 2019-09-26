from django.db import models

# Create your models here.

class ShortModel(models.Model):  # creating a model class short_url to store both original url and sort url
    short_url = models.CharField(max_length=30,unique=True) # will store the newly genrated url
    long_url = models.URLField("Url", unique=True) # will stroe original url which will have unique=True where all the url are unique


