from django.contrib import admin

# Register your models here.
from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", 
                    "price", 
                    "section", 
                    "reduction", 
                    "date_created", 
                    "date_updated"
                    )