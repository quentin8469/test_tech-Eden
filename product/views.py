from rest_framework import viewsets, permissions
from product.models import Product
from product.serializers import ProductSerializer


# Create your views here.

class ProductViewset(viewsets.ModelViewSet):
    """ 
    API end point that allows products to be wiev by authenticated users
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filterset_fields = ['name', 'price', 'section']
    #premission_classe = [permissions.IsAuthenticated,]