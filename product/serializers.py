from dataclasses import fields
from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """ Serializer for the Product model """
    
    class Meta:
        model = Product
        fields = ['name', 'price','section', 'reduction']