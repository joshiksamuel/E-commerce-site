from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Register(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    Username=models.CharField(max_length=50,null=True)
    Email=models.CharField(max_length=50,null=True)
    Password=models.CharField(max_length=50)
    
    def __str__(self):
        return self.Username

class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    description = models.TextField(null=True)
    price = models.FloatField()
    image = models.ImageField(null=True,blank=True)
    image1 = models.ImageField(null=True,blank=True)
    image2 = models.ImageField(null=True,blank=True)
    image3 = models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.name
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''

        return url
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
   

class shipping(models.Model):
    register= models.ForeignKey(Register,on_delete=models.SET_NULL,null=True,blank=True)
 
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    zipcode=models.IntegerField(null=True)
    namecard=models.CharField(max_length=200)
    creditno=models.CharField(max_length=200)
    expmonth=models.CharField(max_length=200)
    expyear=models.IntegerField(null=True)
    cvv=models.IntegerField(null=True)
    
    def __str__(self):
        return self.name




class Contact(models.Model):
    register= models.ForeignKey(Register,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=50)
    phoneno=models.IntegerField(null=True)
    email=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    message=models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name
    


