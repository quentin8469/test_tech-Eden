from django.contrib import admin

# Register your models here.
from user.models import CustomUser


@admin.register(CustomUser)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("username", "email",)