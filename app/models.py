from django.db import models

# Create your models here.
class Trip(models.Model):
    phonenumber = models.CharField(max_length=60, null=True)
    email = models.EmailField(max_length=40,null=True)
    trip_begin = models.DateTimeField(null=True)
    trip_end = models.DateTimeField(null=True)
    budget = models.IntegerField(max_length=10,null=True)
    destination = models.CharField(max_length=30,null=True)
    guests = models.IntegerField(max_length=10,null=True)

class Hotel(models.Model):
    tripid = models.ForeignKey(Trip)
    link = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=50,null=True)
    reservation = models.CharField(max_length=40,null=True)
    date_begin = models.DateTimeField(null=True)
    date_end = models.DateTimeField(null=True)

class Flight(models.Model):
    tripid = models.ForeignKey(Trip)
    link = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=50,null=True)
    reservation = models.CharField(max_length=40,null=True)
    date = models.DateTimeField(null=True)

class Restaurant(models.Model):
    tripid = models.ForeignKey(Trip)
    link = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=50,null=True)
    reservation = models.CharField(max_length=40,null=True)
    date = models.DateTimeField(null=True)
