# coding=utf-8 
from django.shortcuts import render_to_response
from django.template import loader, Context, RequestContext
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.utils import simplejson as json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
 
#my
from myapp.models import Trip
from myapp.forms import TripForm
from myapp.translate.localize import *

import datetime
from datetime import date, timedelta

def add(request):
	print '--------------------------------> call add'

	if request.method == 'POST':
		form = TripForm(request.POST, request=request)
		
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/index/')
	else:
		form = TripForm()
		
	c = {
		'form':form, 
		'time_translate':DEFAULT_TIME, 
		'date_translate':DEFAULT_DATE,
		'controls_translate':DEFAULT_CONTROLS,
		'startdate':datetime.datetime.today().strftime(DEFAULT_DATETIME_FORMAT_CLIENT),
	}
	
	return render_to_response('add.html', c, RequestContext(request))

def set_session(request):
	print '--------------------------------> call set_session'
	
	format = DEFAULT_DATE.get('pythonDateFormat', DEFAULT_DATETIME_FORMAT_CLIENT)
	
	request.session['startdate'] = datetime.datetime.strptime(request.GET['startdate'], format)	
	request.session['enddate'] = datetime.datetime.strptime(request.GET['enddate'], format)
	request.session['place_from'] = request.GET.get('place_from', '')
	request.session['place_to'] = request.GET.get('place_to', '')
	
	return render_to_response('add.html', RequestContext(request))

def index(request):
	print '--------------------------------> call index'
	#print request.session['startdate']
	
	if request.session.get('startdate', '') != '':
		startdate = request.session.get('startdate', '')
	else:
		startdate = date.today()
		
	if request.session.get('enddate', ''):
		enddate = request.session.get('enddate', '')
	else:
		enddate = startdate + timedelta(days=7)
	
	place_from = request.session.get('place_from', '')
	place_to = request.session.get('place_to', '')
	
	trips = Trip.objects.filter(date__range=[startdate, enddate], place_from=place_from, place_to=place_to)
	Citites = dict(DEFAULT_CITY); 

	data = {
		'trips':trips, 
		'startdate':startdate.strftime(DEFAULT_DATETIME_FORMAT_CLIENT),
		'enddate':enddate.strftime(DEFAULT_DATETIME_FORMAT_CLIENT),
		'place_from':place_from,
		'place_to':place_to,
		'cities':Citites,
		'time_translate':DEFAULT_TIME, 
		'date_translate':DEFAULT_DATE,
		'controls_translate':DEFAULT_CONTROLS,
	}

	return render_to_response('index.html', data, RequestContext(request))

def search(request):
	print '--------------------------------> call search'
	
	startdate = datetime.datetime.strptime(request.GET['date_from'], DEFAULT_DATETIME_FORMAT_SERVER)
	enddate = datetime.datetime.strptime(request.GET['date_to'], DEFAULT_DATETIME_FORMAT_SERVER)
	
	place_from_r = request.GET.get('place_from', '')
	place_to_r = request.GET.get('place_to', '')

	#, place_from=request.GET['place_to'], place_from=request.GET['place_to']
	trips = Trip.objects.filter(date__range=[startdate, enddate], place_from=place_from_r, place_to=place_to_r)

	data = {
		'startdate':startdate, 
		'enddate':enddate,
	}
	
	json_serializer = serializers.get_serializer("json")()
	jsonlist = [
		json_serializer.serialize(trips), 
		[json.dumps(data, cls=DjangoJSONEncoder)],
	]

	return HttpResponse(json.dumps(jsonlist))

def test_template(request):
	trips = Trip.objects.all()
	return render_to_response('test_template.html', {'trips':trips}, RequestContext(request))
