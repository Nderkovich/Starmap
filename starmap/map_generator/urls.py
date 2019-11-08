from django.urls import path
from . import views


app_name = 'map_generator'


urlpatterns = [
    path('', views.start_page, name='main'),
    path('pdf/<int:order_id>/', views.pdf, name='pdf'),
]
