from django.urls import path
from .views import Fruits_view,product_data,vegetable_data,print_req,dry_fruits_data,juices_data
urlpatterns=[
    path('fruits/',Fruits_view),
    path('data/',product_data,name="data_add"),
    path('vegetable/',vegetable_data,name="veg"),
    path('dry-fruits/',dry_fruits_data),
    path('juices/',juices_data),
    path('prints/',print_req,name='total_cart')
]