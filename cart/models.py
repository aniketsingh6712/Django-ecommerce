from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from products.models import Cart
class UserAddress(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    state=models.CharField(max_length=30)
    street1=models.TextField()
    street2=models.TextField()
    
    city=models.CharField(max_length=30)
    pincode=models.CharField(max_length=6)
    Phone=models.CharField(max_length=10)
class Delivery(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.ForeignKey(UserAddress,on_delete=models.CASCADE)
    product=models.JSONField()
    total_amt=models.FloatField()
    payment=models.CharField(max_length=20)

    

