from django.test import TestCase
from market.models import ProductCategory, Product
from datetime import datetime



class ProductListTestCase(TestCase):

    def test_product_list_success(self):
        response = self.client.get('/products/')

        self.assertEqual(response.status_code, 200)



class PeoductDetailTestCase(TestCase):
    def test_product_detail_success(self):
        some_date = datetime(year=2020, month=4, day=4)
        cat1 = ProductCategory.objects.create(name='Посуда')

        product = Product.objects.create(
            category=cat1,
            name='Чайник',
            price=1500,
            sales_percent=None,
            description='Хороший Чайник я сам пользуюсь',
            new_expiry_date=some_date,
            preview_image='/media/jufhrfr.jpeg'

        )

        response = self.client.get(f'/products/{product.id}/')

        self.assertEqual(response.status_code, 200)




