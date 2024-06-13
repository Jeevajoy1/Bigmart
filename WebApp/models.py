from django.db import models

# Create your models here.
class Contactdb(models.Model):
    name=models.CharField(max_length=100,null=True, blank=True)
    email=models.EmailField(max_length=100,null=True, blank=True)
    subject=models.CharField(max_length=100,null=True, blank=True)
    message=models.TextField(max_length=100,null=True, blank=True)
    mobile=models.IntegerField(null=True, blank=True)

class Registerdb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)

class Cartdb(models.Model):
    uname=models.CharField(max_length=100,null=True,blank=True)
    productname=models.CharField(max_length=100,null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    totalprice=models.IntegerField(null=True,blank=True)

class Orderdb(models.Model):
    order_username=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    bill=models.TextField(max_length=100,null=True,blank=True)
    totalprice=models.IntegerField(null=True,blank=True)
