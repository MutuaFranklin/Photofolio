from django.test import TestCase
from .models import Location,Categories,Image
import datetime as dt
# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(location_name='Westlands')

    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    def tearDown(self):
        Location.objects.all().delete()

    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_method(self):
        self.location.save_location()
        self.location.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)

    
    def test_update_location(self):
        self.location.save_location()
        self.location.update_location(self.location.id, 'Parklands')
        updated_location = Location.objects.get(location_name = "Parklands")
        self.assertEqual(updated_location.location_name, 'Parklands')

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

    def test_update_category(self):
        self.Nature.save_category()
        self.Nature.update_category(self.Nature.id, 'Environment')
        updated_category = Categories.objects.get(category = "Environment")
        self.assertEqual(updated_category.category, 'Environment')


    def test_delete_method(self):
        self.Nature.save_category()
        self.Nature.delete_category()
        category = Categories.objects.all()
        self.assertTrue(len(category)==0)

class ImageTestClass(TestCase):
    def setUp(self):
        self.test_category = Categories(category='Indoor')
        self.test_category.save_category()

        self.location = Location(location_name="Westlands")
        self.location.save_location()

        self.image = Image(id=1, image = 'kanye.jpg',image_name="Kanye",image_category=self.test_category,image_location=self.location,)
        self.image.save_image()

    def tearDown(self):
        Categories.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_display_all_image_items(self):
        images = self.image.display_all_image_items()
        self.assertTrue(len(images)>0)

    def test_update_image(self):
        self.image.save_image()
        image_id = Image.objects.last().id
        Image.update_image(image_id,'drake' )
        updated_image = Image.objects.get(id=image_id)
        self.assertEqual(updated_image.image_name,'drake')

        

    def test_delete_method(self):
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)

    def test_get_image_by_id(self):
        got_image= self.image.get_image_by_id(self.image.id)
        self.assertTrue(len(got_image)==1)


    def test_search_by_category(self):
        category_images=self.image.search_by_category(self.test_category)
        self.assertTrue(len(category_images)>0)

    def test_filter_by_location(self):
        location_images = self.image.filter_by_location(self.location)
        self.assertTrue(len(location_images)>0)

    def test_filter_by_category(self):
        cat_images = self.image.filter_by_category(self.test_category)
        self.assertTrue(len(cat_images)>0)





