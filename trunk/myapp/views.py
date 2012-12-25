# coding=utf-8 
from django.shortcuts import render_to_response
from django.template import loader, Context, RequestContext
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.utils import simplejson as json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.db.models import Q
 
#my
from myapp.models import Trip
from myapp.forms import TripForm
from myapp.translate.localize import *

import operator
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
	
	startdate = request.session.get('startdate', '') if request.session.get('startdate', '') != '' else date.today()
	enddate = request.session.get('enddate', '') if request.session.get('enddate', '') else startdate + timedelta(days=7)

	data = {
		'startdate':startdate.strftime(DEFAULT_DATETIME_FORMAT_CLIENT),
		'enddate':enddate.strftime(DEFAULT_DATETIME_FORMAT_CLIENT),
		'place_from':request.session.get('place_from', ''),
		'place_to':request.session.get('place_to', ''),
		'cities':dict(DEFAULT_CITY),
		'time_translate':DEFAULT_TIME, 
		'date_translate':DEFAULT_DATE,
		'controls_translate':DEFAULT_CONTROLS,
	}

	return render_to_response('index.html', data, RequestContext(request))

def search(request):
	print '--------------------------------> call search'
	
	#dates
	if request.GET.get('date_from', '') == '':
		date_from = request.session.get('startdate', '') if request.session.get('startdate', '') != '' else date.today()
	else:
		date_from = json.loads(request.GET['date_from'])
		
	if request.GET.get('date_to', '') == '':
		date_to = request.session.get('enddate', '') if request.session.get('enddate', '') else startdate + timedelta(days=7)
	else:
		date_to = json.loads(request.GET['date_to'])

	#places
	if request.GET.get('place_from', '') == '':
		place_from = request.session.get('place_from', '')
	else:
		place_from = json.loads(request.GET['place_from'])

	if request.GET.get('place_to', '') == '':
		place_to = request.session.get('place_to', '')
	else:
		place_to = json.loads(request.GET['place_to'])
		
	# by many filters
	if isinstance(date_from, list):
		q_list = [Q(date__range=[datetime.datetime.strptime(date_from[i], DEFAULT_DATETIME_FORMAT_SERVER), 
								 datetime.datetime.strptime(date_to[i], DEFAULT_DATETIME_FORMAT_SERVER)], 
					place_from=place_from[i], 
					place_to=place_to[i]) for i in range(date_from.__len__())]
				
		trips = Trip.objects.filter(reduce(operator.or_, q_list))

		data = {
			'startdate':datetime.datetime.strptime(date_from[0], DEFAULT_DATETIME_FORMAT_SERVER), 
			'enddate':datetime.datetime.strptime(date_to[0], DEFAULT_DATETIME_FORMAT_SERVER),
		}
	# by one filter
	else:
		trips = Trip.objects.filter(date__range=[date_from, date_to], place_from=place_from, place_to=place_to)

		data = {
			'startdate':date_from.strftime(DEFAULT_DATETIME_FORMAT_CLIENT),
			'enddate':date_to.strftime(DEFAULT_DATETIME_FORMAT_CLIENT),
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
