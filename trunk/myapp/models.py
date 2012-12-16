from django.db import models
from django.contrib import admin
from phonenumber_field.modelfields import PhoneNumberField

LithuaniaCities = (
	('Visagines', 'Visagines') ,
	('Draunas', 'Draunas'),
	('Kaunas', 'Kaunas'),
	('Vilnus', 'Vilnus'),
)

class Trip(models.Model):
	name = models.CharField(max_length=150)
	place_from = models.CharField(max_length=150, choices=LithuaniaCities)
	place_to = models.CharField(max_length=150, choices=LithuaniaCities)
	comments = models.TextField()
	phone_number = PhoneNumberField()
	date = models.DateTimeField()

	class Meta:
		ordering = ["date"]

class TripAdmin(admin.ModelAdmin):
	list_display = ('name', 'place_from', 'place_to', 'phone_number', 'date', )

admin.site.register(Trip, TripAdmin)