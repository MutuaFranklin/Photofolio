from django.test import TestCase
from .models import Location,Categories,Image
import datetime as dt
# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.Westlands = Location(location='Westlands')

    def test_instance(self):
        self.assertTrue(isinstance(self.Westlands,Location))

    def tearDown(self):
        Location.objects.all().delete()

    def test_save_method(self):
        self.Westlands.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_method(self):
        self.Westlands.delete_location('Moringa')
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)

class categoriesTestClass(TestCase):
    def setUp(self):
        self.Nature = Categories(category='Nature')

    def test_instance(self):
        self.assertTrue(isinstance(self.Nature,Categories))

    def tearDown(self):
        Categories.objects.all().delete()

    def test_save_method(self):
        self.Nature.save_category()
        category = Categories.objects.all()
        self.assertTrue(len(category)>0)

    def test_delete_method(self):
        self.Nature.delete_category('Nature')
        category = Categories.objects.all()
        self.assertTrue(len(category)==0)

class ImageTestClass(TestCase):
    def setUp(self):
        self.test_category = Categories(category=list('Indoor'))
        self.test_category.save_category()

        self.location = Location(location="Westlands")
        self.location.save_location()

        self.image = Image(id=1,title="Slide Away",categories=self.test_category,location=self.location,)
        self.image.save_image()

    def tearDown(self):
        Categories.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()
