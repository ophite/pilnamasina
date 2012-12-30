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
		'date_from':datetime.datetime.today().strftime(DEFAULT_DATETIME_FORMAT_CLIENT),
	}
	
	return render_to_response('add.html', c, RequestContext(request))

def set_session(request):
	print '--------------------------------> call set_session'
	
#	format = DEFAULT_DATE.get('pythonDateFormat', DEFAULT_DATETIME_FORMAT_CLIENT)
	
#	request.session['date_from'] = datetime.datetime.strptime(request.GET['date_from'], format)	
#	request.session['date_to'] = datetime.datetime.strptime(request.GET['date_to'], format)
#	request.session['place_from'] = request.GET.get('place_from', '')
#	request.session['place_to'] = request.GET.get('place_to', '')
		
	request.session['date_from'] = [datetime.datetime.strptime(date, DEFAULT_DATETIME_FORMAT_SERVER) for date in json.loads(request.GET.get('date_from', ''))]
	request.session['date_to'] = [datetime.datetime.strptime(date, DEFAULT_DATETIME_FORMAT_SERVER) for date in json.loads(request.GET.get('date_to', ''))]
	request.session['place_from'] = json.loads(request.GET.get('place_from', ''))
	request.session['place_to'] = json.loads(request.GET.get('place_to', ''))
	
	return render_to_response('add.html', RequestContext(request))

def index(request):
	print '--------------------------------> call index'
	
	data = {
		'cities':dict(DEFAULT_CITY),
		'time_translate':DEFAULT_TIME, 
		'date_translate':DEFAULT_DATE,
		'controls_translate':DEFAULT_CONTROLS,
	}

	return render_to_response('index.html', data, RequestContext(request))

def tryStringToDate(str, default, format):
	try:
		return datetime.datetime.strptime(str, format)
	except ValueError:
		return default 
		
def search(request):
	print '--------------------------------> call search'
 
	#dates
	if request.GET.get('date_from', '') == '':
		date_from = request.session.get('date_from', [datetime.date.today()])
	else:
		date_from = [tryStringToDate(date, datetime.date.today(), DEFAULT_DATETIME_FORMAT_SERVER) for date in json.loads(request.GET['date_from'])]

	if request.GET.get('date_to', '') == '':
		date_to = request.session.get('date_to', [datetime.date.today() + datetime.timedelta(days=7)])
	else:
		date_to = [tryStringToDate(date, datetime.date.today(), DEFAULT_DATETIME_FORMAT_SERVER) for date in json.loads(request.GET['date_to'])]

	#places
	if request.GET.get('place_from', '') == '':
		place_from = request.session.get('place_from', '')
	else:
		place_from = json.loads(request.GET['place_from'])

	if request.GET.get('place_to', '') == '':
		place_to = request.session.get('place_to', '')
	else:
		place_to = json.loads(request.GET['place_to'])
	
	filters = {
		'date_from':json.dumps([d.strftime(DEFAULT_DATETIME_FORMAT_CLIENT) for d in date_from], cls=DjangoJSONEncoder),
		'date_to':json.dumps([d.strftime(DEFAULT_DATETIME_FORMAT_CLIENT) for d in date_to], cls=DjangoJSONEncoder),
		'place_from':json.dumps(request.session.get('place_from', ''), cls=DjangoJSONEncoder),
		'place_to':json.dumps(request.session.get('place_to', ''), cls=DjangoJSONEncoder),
	}
	
	# by many filters
	if isinstance(date_from, list):
		q_list = [Q(date__range=[date_from[i], date_to[i]], 
					place_from=place_from[i], 
					place_to=place_to[i]) for i in range(date_from.__len__())]
				
		trips = Trip.objects.filter(reduce(operator.or_, q_list))
		data = {
			'date_from':date_from[0], 
			'date_to':date_to[0],
		}
	# by one filter
	else:
		trips = Trip.objects.filter(date__range=[date_from, date_to], place_from=place_from, place_to=place_to)
		data = {
			'date_from':date_from.strftime(DEFAULT_DATETIME_FORMAT_CLIENT),
			'date_to':date_to.strftime(DEFAULT_DATETIME_FORMAT_CLIENT),
		}
		
	json_serializer = serializers.get_serializer("json")()
	jsonlist = [
		json_serializer.serialize(trips), 
		json.dumps(data, cls=DjangoJSONEncoder),
		json.dumps(filters, cls=DjangoJSONEncoder),
	]

	return HttpResponse(json.dumps(jsonlist))

def test_template(request):
	trips = Trip.objects.all()
	return render_to_response('test_template.html', {'trips':trips}, RequestContext(request))
