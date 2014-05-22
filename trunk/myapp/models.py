# coding=utf-8
from django.db import models
from django.contrib import admin
from phonenumber_field.modelfields import PhoneNumberField
from myapp.translate.localize import *

class TripManager(models.Manager):
    def create_trip(self, date, type, place_from, place_to, name, phone_number, comments):
        trip = self.create(date=date, type=type, place_from=place_from, place_to=place_to, name=name, phone_number=phone_number, comments=comments)
        return trip

class Trip(models.Model):
	date = models.DateTimeField()
	type = models.CharField(max_length=150, choices=DEFAULT_TRIPTYPE)
	place_from = models.CharField(max_length=19, choices=DEFAULT_CITY)
	place_to = models.CharField(max_length=19, choices=DEFAULT_CITY)
	name = models.CharField(max_length=50)
	phone_number = PhoneNumberField()
	comments = models.TextField(max_length=200, null=True, blank=True)

	class Meta:
		ordering = ["date"]

	# def __str__(self):
	# 	return "place_from:{0} place_to:{1} date:{2} phone_number:{3} name:{4} type:{5} comments:{6}".format(self.place_from, 
	# 		self.place_to.encode('utf-8'), 
	# 		str(self.date), 
	# 		self.phone_number, 
	# 		self.name.encode('utf-8'), 
	# 		self.type.encode('utf-8'), 
	# 		self.comments.encode('utf-8'))
	def __unicode__(self):
		text = "phone_number:" + str(self.phone_number)
		return text
		# return "place_from:{0} place_to:{1} date:{2} phone_number:{3} name:{4} type:{5} comments:{6}".format(
		# 	self.place_from.encode('utf-8'), 
		# 	self.place_to.encode('utf-8'), 
		# 	str(self.date), 
		# 	self.phone_number, 
		# 	self.name.encode('utf-8'), 
		# 	self.type.encode('utf-8'), 
		# 	self.comments.encode('utf-8'))

	objects = TripManager()

class TripAdmin(admin.ModelAdmin):
	list_display = ('name', 'place_from', 'place_to', 'phone_number', 'date', 'type', )

admin.site.register(Trip, TripAdmin)