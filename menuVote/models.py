from datetime import date

from django.db import models


class Restaurant(models.Model):
	name = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	phone_number = models.CharField(max_length=20)


class Menu(models.Model):
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	date = models.DateField(default=date.today)
	items = models.TextField()


class Employee(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)


class Vote(models.Model):
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	vote = models.BooleanField(default=False)
