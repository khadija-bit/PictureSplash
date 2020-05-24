from django.db import models

#Create your models here.
class Location(models.Model):
    location = models.CharField(max_length = 60)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save    

class Category(models.Model):
    category = models.CharField(max_length = 60)

    def __str__(self):
        return self.category
    
    def save_category(self):
        self.save  
