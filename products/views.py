from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
import requests

from django.http import JsonResponse
from .models import Product
from .models import Cart
def Fruits_view(request):
    obj=Product.objects.all().filter(category="fruits")
    context={'api_data':obj}
    return render(request,'products/products.html',context)


def product_data(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        dt=data.strip("[]").split(",")
        name,id,price,category,imageUrl=dt
        
        if request.user.is_authenticated:
            product=Product.objects.get(id=id)
            product_check=Cart.objects.filter(userid=request.user,product=product)
            if product_check.exists():
                 product_check=Cart.objects.get(userid=request.user,product=product)
                 qty=product_check.quantity+1
                 total=product_check.product.price *qty
                 product_check.quantity=qty
                 product_check.total_price=total
                 product_check.save()
                
                 return JsonResponse({'status': 'success', 'message': "quantity is updated"})

            obj=Cart.objects.create(userid=request.user,product=product,quantity=1,url=imageUrl,total_price=product.price)
            return JsonResponse({'status': 'success', 'message': "added"})
        return JsonResponse({'status': 'success', 'message': "Please Login"})
def vegetable_data(request):
        obj=Product.objects.all().filter(category="vegetable")
        context={'api_data':obj}
        return render(request,'products/products.html',context)
def dry_fruits_data(request):
     obj=Product.objects.all().filter(category="dry-fruits")
     context={'api_data':obj}
     return render(request,'products/products.html',context)
def juices_data(request):
     obj=Product.objects.all().filter(category="juices")
     context={'api_data':obj}
     return render(request,'products/products.html',context)

def print_req(request):
     ob=Cart.objects.all()
     cart_total=0
     for obj in ob:
          cart_total+=obj.quantity
     print(ob[0].userid.email)
     return redirect('/')
