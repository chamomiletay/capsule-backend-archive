import imp
from django.contrib import admin
#--import models --
from .models import Article

# Register your models here.
admin.site.register(Article)