from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User_Message(models.Model):
    name = models.CharField(max_length=60)
    phone = PhoneNumberField(unique=True)
    message = models.TextField(max_length=600)
    
    def __str__(self):
        return self.name    


class Reservation(models.Model):
    FIO = models.CharField(max_length=150)
    phone = PhoneNumberField(unique=True)
    email = models.CharField(max_length=60)
    guests = models.IntegerField()
    time = models.CharField(max_length=20)
    comment = models.TextField(max_length=2500)

    def __str__(self):
        return self.FIO


class Dish(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to = 'site_images/', blank = True)
    description = models.CharField(max_length=300)
    sort = models.CharField(default='', max_length=60)
    weight = models.IntegerField(default=300)

    def __str__(self):
        return self.name


class Wine(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to = 'site_images/', blank = True)
    description = models.CharField(max_length=300)
    sort = models.CharField(default='', max_length=60)
    amount = models.IntegerField(default=1000)
    
    def __str__(self):
        return self.name    
