from django.shortcuts import render
from cart.models import Delivery
# Create your views here.
def User_details(request):
    if request.user.is_authenticated:
        delivery=Delivery.objects.filter(userid=request.user)
        
        return render(request,'user/user.html',{'deliverys':delivery})
