from django.shortcuts import render
from products.models import Product


def shop_page(request):
    
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'shop/shop.html', context)




