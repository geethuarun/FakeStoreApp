from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=200,unique=True)
    is_active=models.BooleanField(default=True)


    def __str__(self):
        return self.name
    
class Products(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=300)
    picture=models.ImageField(upload_to="images")
    price=models.PositiveIntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
class Carts(models.Model):
    product=models.ForeignKey(Products,on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(("in-cart","in-cart"),
             ("order-placed","order-placed"),
             ("cancelled","cancelled"))
    status=models.CharField(max_length=200,choices=options,default="in-cart")


class Orders(models.Model):
    products=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(("dispatched","dispatched"),
             ("order-placed","order-placed"),
             ("cancelled","cancelled"))
    status=models.CharField(max_length=200,choices=options,default="order-placed")

from django.core.validators import MinValueValidator,MaxValueValidator
class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    comment=models.CharField(max_length=300)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])



