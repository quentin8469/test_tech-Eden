from django.db import models
from django.conf import settings
from product.models import Product
# Create your models here.

class Cart(models.Model):
    """ A model for the market cart """
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    
    
    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"


class CartProduct(models.Model):
    """A model for the products cart """
    
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name = "Cart Product"
        verbose_name_plural = "Cart Products"


class Ticket(models.Model):
    """ A model for payment summary"""
    
    product_cost = models.DecimalField(max_digits=10, decimal_places=2)
    reduc_cost = models.DecimalField(max_digits=10, decimal_places=2)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    
    
    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"