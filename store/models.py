from django.db import models

# Create your models here.

class Users(models.Model):
	fname = models.CharField(max_length=200)
	lname = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	address_line = models.CharField(max_length=200)
	postcode = models.CharField(max_length=200)
	password = models.CharField(max_length=200)

	