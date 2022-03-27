from rest_framework import viewsets, permissions

from product.models import Product
from product.serializers import ProductSerializer



# Create your views here.

class ProductViewset(viewsets.ModelViewSet):
    """ 
    API end point that allows products to be view by authenticated users
    """
    premission_classe = [permissions.IsAuthenticated,]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filterset_fields = ['name', 'price', 'section']
    search_fields = ['name', 'price', 'section']
    