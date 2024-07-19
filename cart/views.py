from django.shortcuts import render,redirect
from products.models import Cart
from django.http import JsonResponse
from django.urls import reverse
from django.db.models import Sum
from .models import UserAddress
from .models import Delivery
from products.models import Cart
from django.contrib import messages
# Create your views here.
def cart_page(request):
    if request.user.is_authenticated:
        total_price = Cart.objects.filter(userid=request.user).aggregate(total=Sum('total_price'))['total']
        cart_item=Cart.objects.filter(userid=request.user)
        price_after_check=0
        if total_price:
            price_after_check=total_price+120-30
        return render(request, 'cart/cart.html',{'cart_item':cart_item,'total_price':total_price,'price_after_check':price_after_check})
    else:
        
        return redirect('/')

def checkout(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            state=request.POST['state']
            street1 = request.POST['street1']
            street2 = request.POST['street2']
            city = request.POST['city']
            pincode = request.POST['pincode']
            phone = request.POST['phone']
            address=UserAddress.objects.filter(userid=request.user)
            if len(phone)!=10:
                messages.info(request,"Phone number is not correct")
                return redirect('/cart/checkout')
            if len(pincode)!=6:
                messages.info(request,"Pincode is not correct")
                return redirect('/cart/checkout')
            if address.exists():
                address=UserAddress.objects.get(userid=request.user)
                address.first_name=firstname
                address.last_name=lastname
                address.state=state
                address.street1=street1
                address.street2=street2
                address.city=city
                address.pincode=pincode
                address.Phone=phone
                address.save()
            else:
                UserAddress.objects.create(userid=request.user,first_name=firstname,last_name=lastname,state=state,street1=street1,street2=street2,city=city,pincode=pincode,Phone=phone)
            return redirect('/cart/checkout')
        address=UserAddress.objects.filter(userid=request.user)[0]
        total_price = Cart.objects.filter(userid=request.user).aggregate(total=Sum('total_price'))['total']
        price_after_check=0
        if total_price:
            price_after_check=total_price+120-30
        if address:
            return render(request, 'cart/checkout.html',{'address':address,'total_price':total_price,'price_after_check':price_after_check})
        else:
            return render(request, 'cart/checkout.html')
            

def operation_view(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        dt=data.strip("[]").split(",")
        id,op=dt
        obj=Cart.objects.get(userid=request.user,id=int(id))
        
        
        redirect_url=reverse('cart')
        
        if op=='add':
           
            qty=obj.quantity+1
            total=(obj.product.price) *qty
            obj.quantity=qty
            obj.total_price=total
            obj.save()
            
        elif op=='sub' and obj.quantity>1:
            qty=obj.quantity-1
            total=(obj.product.price) *qty
            obj.quantity=qty
            obj.total_price=total
            obj.save()
        elif op=='sub' and obj.quantity==1:
            obj.delete()
        elif op=='remove':
            obj.delete()
        
        return JsonResponse({'redirect_url':redirect_url})

def delivery_details(request):
    if request.method=="POST":
        
        payment = request.POST['optradio']
        address=UserAddress.objects.filter(userid=request.user)[0]
        
        total_price = Cart.objects.filter(userid=request.user).aggregate(total=Sum('total_price'))['total']
        if total_price:
            total=total_price+120-30
            products=Cart.objects.filter(userid=request.user)
            
            l=[]
            for product in products:
                dict={}
                dict['name']=product.product.name
                dict['qty']=product.quantity
                l.append(dict)
            delivery=Delivery.objects.create(userid=request.user,address=address,product=l,total_amt=total,payment=payment)
            delivery.save()
        else:
            
            return redirect('/cart/checkout')
        

    obj=Cart.objects.filter(userid=request.user)
    obj.delete()
    return redirect('/')