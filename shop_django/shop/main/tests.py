from rest_framework.test import APITestCase
from django.test import TestCase
from .models import Categories, Products, Manufactures

class CategoriesTest(TestCase):
    pass


class ProductTest(APITestCase):
    def setUp(self):
        Products.objects.create()