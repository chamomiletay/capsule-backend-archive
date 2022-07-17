from email.mime import image
from io import BufferedRandom
from turtle import color
from unicodedata import category
from django.db import models

# Create your models here.

class Article(models.Model):
    name = models.TextField()
    color = models.TextField()
    image = models.ImageField()
    article_type = models.TextField()
    category = models.TextField()
    brand = models.TextField()
    quantity = models.TextField()

    def __str__(self):
        return self.name