# coding=utf-8
from django.db import models
from django.contrib import admin
from phonenumber_field.modelfields import PhoneNumberField
from myapp.translate.localize import *

class Trip(models.Model):
	name = models.CharField(max_length=150)
	place_from = models.CharField(max_length=150, choices=DEFAULT_CITY)
	place_to = models.CharField(max_length=150, choices=DEFAULT_CITY)
	comments = models.TextField(max_length=200, null=True, blank=True)
	phone_number = PhoneNumberField()
	date = models.DateTimeField()

	class Meta:
		ordering = ["date"]

class TripAdmin(admin.ModelAdmin):
	list_display = ('name', 'place_from', 'place_to', 'phone_number', 'date', )

admin.site.register(Trip, TripAdmin)