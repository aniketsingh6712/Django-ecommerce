from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_page, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('operation',views.operation_view,name='operations'),
     path('delivery/',views.delivery_details,name='delivery')
]
