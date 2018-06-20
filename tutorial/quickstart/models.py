from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	profileimage = models.TextField()
	username = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	
	mobile = models.IntegerField()


class Shop(models.Model):
	category = models.CharField(max_length=200)
	
	location = models.TextField()
	area = models.CharField(max_length=200)
	UnitPrice = models.IntegerField()
	SellingPrice = models.IntegerField()




class Product(models.Model):
	name = models.CharField(max_length=200)
	
	description = models.TextField()
	sku = models.CharField(max_length=200)
	variant = models.CharField(max_length=200)
	UnitPrice = models.IntegerField()
	SellingPrice = models.IntegerField()





