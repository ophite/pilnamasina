# coding=utf-8 
from django.shortcuts import render_to_response
from django.template import loader, Context, RequestContext
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.utils import simplejson as json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.db.models import Q
from django.utils.datastructures import SortedDict

#my
from myapp.models import Trip
from myapp.forms import TripForm
from myapp.translate.localize import *

import operator
import datetime
from datetime import date, timedelta

def tryStringToDate(str, default, format):
	try:
		return datetime.datetime.strptime(str, format)
	except ValueError:
		return default 

def get_sort_tuple_first(tuple):
	keys = dict(tuple).keys()
	keys.sort()
	first = dict(tuple)[keys[0]]
	
	return first

def add(request):
	print '--------------------------------> call add'

#	TODO Button cancel click 
#	u'delete' in request.POST or 
	if u'delete.x' in request.POST :
		return HttpResponseRedirect('/')
	
	if request.method == 'POST':
		form = TripForm(request.POST, request=request)
		
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = TripForm()
		
	c = {
		'form':form, 
		'time_translate':DEFAULT_TIME, 
		'date_translate':DEFAULT_DATE,
		'controls_translate':DEFAULT_CONTROLS,
		'date_from':datetime.datetime.today().strftime(DEFAULT_DATETIME_FORMAT_CLIENT),
		'phonenumber': DEFAULT_PHONEPREFIX,
	}
	
	return render_to_response('add.html', c, RequestContext(request))

def set_session(request):
	print '--------------------------------> call set_session'
	
#	format = DEFAULT_DATE.get('pythonDateFormat', DEFAULT_DATETIME_FORMAT_CLIENT)
	
	any_city = get_sort_tuple_first(DEFAULT_CITY)
	any_type = get_sort_tuple_first(DEFAULT_TRIPTYPE)
	
	request.session['date_from'] = [tryStringToDate(date, datetime.date.today(), DEFAULT_DATETIME_FORMAT_SERVER) for date in json.loads(request.GET.get('date_from', ''))]
	request.session['date_to'] = [tryStringToDate(date, datetime.date.today() + datetime.timedelta(days=7), DEFAULT_DATETIME_FORMAT_SERVER) for date in json.loads(request.GET.get('date_to', ''))]
	request.session['place_from'] = json.loads(request.GET.get('place_from', any_city)) #''))
	request.session['place_to'] = json.loads(request.GET.get('place_to', any_city)) #''))
	request.session['type'] = json.loads(request.GET.get('type', any_type))
		
	return render_to_response('add.html', RequestContext(request))

def index(request):
	print '--------------------------------> call index'
	
	data = {
		'cities':dict(DEFAULT_CITY),
		'types':dict(DEFAULT_TRIPTYPE),
		'time_translate':DEFAULT_TIME, 
		'date_translate':DEFAULT_DATE,
		'controls_translate':DEFAULT_CONTROLS,
	}

	return render_to_response('index.html', data, RequestContext(request))
			
def search(request):
	print '--------------------------------> call search'
 
	#dates
	if request.GET.get('date_from', '') == '':
		date_from = request.session.get('date_from', [datetime.date.today()])
	else:
		date_from = [tryStringToDate(date, datetime.date.today(), DEFAULT_DATETIME_FORMAT_SERVER) for date in json.loads(request.GET['date_from'])]

	if request.GET.get('date_to', '') == '':
		date_to = request.session.get('date_to', [datetime.date.today() + datetime.timedelta(days=14)])
	else:
		date_to = [tryStringToDate(date, datetime.date.today() + datetime.timedelta(days=14), DEFAULT_DATETIME_FORMAT_SERVER) for date in json.loads(request.GET['date_to'])]

	#places
	if request.GET.get('place_from', '') == '':
		place_from = request.session.get('place_from', [''])
	else:
		place_from = json.loads(request.GET['place_from'])

	if request.GET.get('place_to', '') == '':
		place_to = request.session.get('place_to', [''])
	else:
		place_to = json.loads(request.GET['place_to'])

	#type
	if request.GET.get('type', '') == '':
		type = request.session.get('type', dict(DEFAULT_TRIPTYPE).keys())
	else:
		type = json.loads(request.GET['type'])
	
	filters = {
		'date_from':json.dumps([d.strftime(DEFAULT_DATETIME_FORMAT_CLIENT) for d in date_from], cls=DjangoJSONEncoder),
		'date_to':json.dumps([d.strftime(DEFAULT_DATETIME_FORMAT_CLIENT) for d in date_to], cls=DjangoJSONEncoder),
		'place_from':json.dumps(request.session.get('place_from', ''), cls=DjangoJSONEncoder),
		'place_to':json.dumps(request.session.get('place_to', ''), cls=DjangoJSONEncoder),
		'type':json.dumps(request.session.get('type', ''), cls=DjangoJSONEncoder),
	}

	type_dict = dict(DEFAULT_TRIPTYPE)
	cities_keys = dict(DEFAULT_CITY).values()
	
	any_city = get_sort_tuple_first(DEFAULT_CITY)
	any_type = get_sort_tuple_first(DEFAULT_TRIPTYPE)
		
	# by many filters
	if isinstance(date_from, list):
		q_list = [Q(type__in = type_dict.keys() if type[0].strip() == any_type.strip() else [k if type_dict[k] == type[0] else '' for k in type_dict],
					date__range=[date_from[i], date_to[i]], 
					place_from__in = cities_keys if place_from[i].strip() == any_city.strip() else (place_from[i],),
					place_to__in = cities_keys if place_to[i].strip() == any_city.strip() else (place_to[i],)) for i in range(date_from.__len__())]
	# by one filter
	#else:
	#	q_list = [Q(date__range=[date_from, date_to], place_from=place_from, place_to=place_to)]

	#print q_list
	trips = Trip.objects.filter(reduce(operator.or_, q_list))
	#trips2 = Trip.objects.all()
	
	json_serializer = serializers.get_serializer("json")()	
	jsonlist = [
		json_serializer.serialize(trips), 
		json.dumps(filters, cls=DjangoJSONEncoder),
	]

	return HttpResponse(json.dumps(jsonlist))

def test_template(request):
	trips = Trip.objects.all()
	return render_to_response('test_template.html', {'trips':trips}, RequestContext(request))
