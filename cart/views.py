from rest_framework import viewsets, permissions
from rest_framework.response import Response
from cart.models import Cart
from cart.serializers import CartSerializer


# Create your views here.

class CartViewset(viewsets.ModelViewSet):
    """ 
    API end point that allows products to be view in cart by authenticated users
    """
    
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    


