from django.test import TestCase
from product.models import Product


class TestProductModels(TestCase):
    """ """

    def test_create_product(self):
        """ """
        product = Product.objects.create(name='test name product', 
                                        price=12, 
                                        section='product section', 
                                        reduction=2.5,
                                         )
        self.assertEqual(product.name, 'test name product')
        product.save()
        