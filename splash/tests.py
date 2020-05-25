from django.test import TestCase
from .models import Location,Category,Image

class LocationTestClass(TestCase):

    def setUp(self):
        self.khadija = Location(location = 'Nairobi')

    def test_instance(self):    
        self.assertTrue(isinstance(self.khadija,Location))
    
    def test_save_location(self):
        self.khadija.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)
    
    def tearDown(self):
        Category.objects.all().delete() 
        Image.objects.all().delete()

class CategoryTestClass(TestCase):

    def setUp(self):
        self.khadija = Category(category = 'Photo')
        
    def test_instance(self):    
        self.assertTrue(isinstance(self.khadija,Category))
    
    def test_save_category(self):
        self.khadija.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)
    def tearDown(self):
        Location.objects.all().delete() 
        Image.objects.all().delete()

class ImageTestClass(TestCase):

    def setUp(self):
        self.khadija = Image(image = 'Photo')
        
    def test_instance(self):    
        self.assertTrue(isinstance(self.khadija,Image))
    
    def test_save_image(self):
        self.khadija.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0)
    def tearDown(self):
        Location.objects.all().delete()         
        Category.objects.all().delete()         
