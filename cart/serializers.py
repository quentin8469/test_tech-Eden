from rest_framework import serializers
from cart.models import Cart
from product.models import Product
from product.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    """ Serialiaze the cart with the products """
    
    products = ProductSerializer(read_only=True, many=True)
    
    class Meta:
        model = Cart
        fields = "__all__"
    