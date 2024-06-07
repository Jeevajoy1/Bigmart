from django.db import models

# Create your models here.
class Catdb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    desc=models.TextField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to= "Cat Images",null=True,blank=True)


class Productdb(models.Model):
    cname=models.CharField(max_length=100,null=True,blank=True)
    pname=models.CharField(max_length=100,null=True,blank=True)
    desc=models.TextField(max_length=100,null=True,blank=True)
    price=models.CharField(max_length=100,null=True,blank=True)
    pimage=models.ImageField(upload_to="Product Images", null=True,blank=True)

