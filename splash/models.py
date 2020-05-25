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

class Image(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length = 30)
    description = models.TextField()
    author = models.CharField(max_length = 30)
    date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    
    

    def __str__(self):
        return self.category
    
    def save_image(self):
        self.save  

    # def delete_image(self):
    #     self.delete 

    