# coding=utf-8
from django.db import models
from django.contrib import admin
from phonenumber_field.modelfields import PhoneNumberField
from myapp.translate.localize import *

class Trip(models.Model):
	date = models.DateTimeField()
	type = models.CharField(max_length=150, choices=DEFAULT_TRIPTYPE)
	place_from = models.CharField(max_length=150, choices=DEFAULT_CITY)
	place_to = models.CharField(max_length=150, choices=DEFAULT_CITY)
	name = models.CharField(max_length=150)
	phone_number = PhoneNumberField()
	comments = models.TextField(max_length=200, null=True, blank=True)

	class Meta:
		ordering = ["date"]

class TripAdmin(admin.ModelAdmin):
	list_display = ('name', 'place_from', 'place_to', 'phone_number', 'date', 'type', )

admin.site.register(Trip, TripAdmin)