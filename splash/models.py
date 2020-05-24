from django.db import models

#Create your models here.
class Location(models.Model):
    location = models.CharField(max_length = 60)

    def __str__(self):
        return self.location

class Category(models.Model):
    category = models.CharField(max_length = 60)

    def __str__(self):
        return self.category