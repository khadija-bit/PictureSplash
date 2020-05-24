from django.test import TestCase
from .models import Location,Category

class LocationTestClass(TestCase):

    def setUp(self):
        self.khadija = Location(location = 'Nairobi')

    def test_instance(self):    
        self.assertTrue(isinstance(self.khadija,Location))
    
    def test_save_location(self):
        self.khadija.save_location()
        location = Location.objects_all()
        self.assertTrue(len(location) > 0)


class CategoryTestClass(TestCase):

    def setUp(self):
        self.khadija = Category(category = 'Photo')
        
    def test_instance(self):    
        self.assertTrue(isinstance(self.khadija,Category))
    
    def test_save_category(self):
        self.khadija.save_category()
        category = Category.objects_all()
        self.assertTrue(len(category) > 0)
