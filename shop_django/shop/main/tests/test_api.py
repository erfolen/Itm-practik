from rest_framework.test import APITestCase
from django.test import TestCase
from django.urls import reverse
from main.models import Categories, Products, Manufactures
from main.serializers import ProductSerializer

class ProductApiTestCAse(APITestCase):
    def test_products_get(self):
        category_1 = Categories.objects.create(name='Диваны')
        product_1 = Products.objects.create(
            name='Угловой диван «Леруа» (2L.90.1R)', article='2L.90.1R', price=6772, quantity=10,
            category=category_1
        )
        product_2 = Products.objects.create(
            name='3-х местный диван «Ален 1»', article='Ален 1', price=2090, quantity=3,
            category=category_1
        )
        url = reverse('products-list')
        response = self.client.get(url)
        serializers_data = ProductSerializer([product_1, product_2], many=True).data
        self.assertEqual(serializers_data, response.data)

    def test_product_get(self):
        category_1 = Categories.objects.create(name='Диваны')
        product_1 = Products.objects.create(
            name='Угловой диван «Леруа» (2L.90.1R)', article='2L.90.1R', price=6772, quantity=10,
            category=category_1
        )

        url = reverse('product-detail')
        response = self.client.get(url)
        serializers_data = ProductSerializer([product_1, product_2], many=True).data
        self.assertEqual(serializers_data, response.data)