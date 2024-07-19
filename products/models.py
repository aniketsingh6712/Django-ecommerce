from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    url=models.URLField()
    price = models.IntegerField()
    details = models.TextField()
    category = models.CharField(max_length=12)
    def __str__(self):
        return self.name

class Cart(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    url=models.URLField()
    total_price=models.FloatField(default=0)
    def __str__(self):
        return self.product.name

