from django.contrib import admin
from .models import OrderPdf, OrderPic

# Register your models here.
@admin.register(OrderPdf)
class OrderPdfAdmin(admin.ModelAdmin):
    list_display = ['map' ,'email', 'first_name', 'last_name', 'phone']

@admin.register(OrderPic)
class OrderPicAdmin(admin.ModelAdmin):
    list_display = ['map', 'address', 'city', 'country', 'postal_index',
                    'email', 'first_name', 'last_name', 'phone']