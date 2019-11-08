from django.urls import path
from . import views


app_name = 'orders'


urlpatterns = [
    path('order_pdf/', views.order_pdf, name="order_pdf"),
    path('order_pic/', views.order_pic, name="order_pic"),
]