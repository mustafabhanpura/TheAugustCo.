from django.db import models
from django.utils import timezone
# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=200,default=None)
    price=models.CharField(max_length=8,default=None)
    #size_no=models.CharField(max_length=10,default=None)
    #discount_no=models.IntegerField()
    #net_amount=models.CharField(max_length=8,default=None)
    time_of_reg = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    prod=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.CharField(max_length=100,default=None)
    size=models.CharField(max_length=100,default=None)
    quantity=models.CharField(max_length=100,default=None)
    disc = models.CharField(max_length=100, default=None)
    discount_offered=models.CharField(max_length=100,default=None)
    net_amount=models.IntegerField(default=None)

    def __str__(self):
        return self.prod


class Quant(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,primary_key=True)
    size_val=models.CharField(max_length=10,default=None)
    quantity=models.CharField(max_length=5,default=None)

    def __str__(self):
        return self.size_val


class Discount(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    discount_code=models.CharField(max_length=10,default=None)
    discount_amt=models.IntegerField()

    def __str__(self):
        return self.discount_code



class Det(models.Model):
    item=models.OneToOneField(Order,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,default=None)
    add=models.TextField(max_length=500,default=None)
    contact=models.CharField(max_length=10,default=None)
    email=models.CharField(max_length=30,default=None)
    mode=models.TextField(max_length=40,default=None)
    deliver=models.CharField(max_length=40,default=None)



