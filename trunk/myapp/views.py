# coding=utf-8 
from django.shortcuts import render_to_response
from django.template import loader, Context, RequestContext
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.db.models import Q
from django.utils.datastructures import SortedDict

# instead of this line. because of django version
# from django.utils import simplejson as json
try:
	import json
except ImportError:
   	from django.utils import simplejson as json

# my
from myapp.models import Trip
from myapp.forms import TripForm, TripFormCaptcha
from myapp.translate.localize import *


import operator
import datetime
from datetime import date, timedelta
from helloworld.settings import DEBUG, TEMPLATE_DIRS, USE_TZ

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

	#new trip logic
	if request.session.get('new_trip_time', None) == None or (datetime.datetime.today() - request.session['new_trip_time']).total_seconds() >= NEW_TRIP_SESSION_DURATION:
		request.session['new_trip_count'] = 0
		request.session['new_trip_time'] = datetime.datetime.today()

	if request.method == 'POST':
		if request.session['new_trip_count'] < NEW_TRIP_COUNT:
			form = TripForm(request.POST, request=request)	
		else:
			form = TripFormCaptcha(request.POST, request=request)	

		if form.is_valid():
			form.save()
			request.session['new_trip_count'] = request.session['new_trip_count'] + 1
			return HttpResponseRedirect('/')
		else:
			request.session['new_trip_time'] = datetime.datetime.today()
	else:
		if request.session.get('new_trip_count', 0) >= NEW_TRIP_COUNT:
			form = TripFormCaptcha()
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
		'DEBUG' : DEBUG,
	}

	return render_to_response('index.html', data, RequestContext(request))

#filters
def getFilter_date_from(request):
	if request.GET.get('date_from', '') == '':
		date_from = request.session.get('date_from', [datetime.date.today()])
	else:
		date_from = [tryStringToDate(date, datetime.date.today(), DEFAULT_DATETIME_FORMAT_SERVER) for date in json.loads(request.GET['date_from'])]

	return date_from

def getFilter_date_to(request):
	if request.GET.get('date_to', '') == '':
		date_to = request.session.get('date_to', [datetime.date.today() + datetime.timedelta(days=7)])
	else:
		date_to = [tryStringToDate(date, datetime.date.today() + datetime.timedelta(days=7), DEFAULT_DATETIME_FORMAT_SERVER) for date in json.loads(request.GET['date_to'])]
		
	return date_to
	
def getFilter_place_from(request):
	any_city = get_sort_tuple_first(DEFAULT_CITY)

	if request.GET.get('place_from', '') == '':
		place_from = request.session.get('place_from', [any_city])
	else:
		place_from = json.loads(request.GET['place_from'])

	return place_from
	
def getFilter_place_to(request):
	any_city = get_sort_tuple_first(DEFAULT_CITY)

	if request.GET.get('place_to', '') == '':
		place_to = request.session.get('place_to', [any_city])
	else:
		place_to = json.loads(request.GET['place_to'])

	return place_to

def getFilter_type(request):
	any_type = get_sort_tuple_first(DEFAULT_TRIPTYPE) #dict(DEFAULT_TRIPTYPE).keys()

	if request.GET.get('type', '') == '':
		type = request.session.get('type', [any_type])
	else:
		type = json.loads(request.GET['type'])

	return type
			
def search(request):
	print '--------------------------------> call search'
 	
	date_from = getFilter_date_from(request)
	date_to = getFilter_date_to(request)
	place_from = getFilter_place_from(request)
	place_to = getFilter_place_to(request)
	type = getFilter_type(request)

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
	]

	return HttpResponse(json.dumps(jsonlist))
			
def getFilters(request):
	print '--------------------------------> call getFilters'
	
	date_from = getFilter_date_from(request)
	date_to = getFilter_date_to(request)
	place_from = getFilter_place_from(request)
	place_to = getFilter_place_to(request)
	type = getFilter_type(request)
	
	filters = {
		'date_from':json.dumps([d.strftime(DEFAULT_DATETIME_FORMAT_CLIENT) for d in date_from], cls = DjangoJSONEncoder),
		'date_to':json.dumps([d.strftime(DEFAULT_DATETIME_FORMAT_CLIENT) for d in date_to], cls = DjangoJSONEncoder),
		'place_from':json.dumps(place_from, cls=DjangoJSONEncoder),
		'place_to':json.dumps(place_to, cls=DjangoJSONEncoder),
		'type':json.dumps(type, cls=DjangoJSONEncoder),
#		'place_from':json.dumps(request.session.get('place_from', ''), cls=DjangoJSONEncoder),
#		'place_to':json.dumps(request.session.get('place_to', ''), cls=DjangoJSONEncoder),
#		'type':json.dumps(request.session.get('type', ''), cls=DjangoJSONEncoder),
	}
 	
	jsonlist = [
		json.dumps(filters, cls=DjangoJSONEncoder),
	]

	return HttpResponse(json.dumps(jsonlist))




# >>>>>>>>>>>>>>>>>>>>>>>>>> 

def test_template(request):
	trips = Trip.objects.all()
	return render_to_response('test_template.html', {'trips':trips}, RequestContext(request))

from django.template import TemplateDoesNotExist 
from django.http import HttpResponse 
import os

def robots(request):
	print '--------------------------------> call robots'
	PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
	#TEMPLATE_DIRS[0].replace('/','\\')
#	print PROJECT_PATH /var/www/domniak/data/www/pilnamasina.lt/myapp
	# 
	try: 
#		return HttpResponse(PROJECT_PATH);
		return HttpResponse(open(PROJECT_PATH.replace('\\','/')+'/templates/robots.txt').read(), 'text/plain') 
	except TemplateDoesNotExist: 
		raise Http404() 		
#	template = PROJECT_PATH + '\\templates\\robots.txt'
#	context = {1:'1'}
#	return render_to_response(template, context, RequestContext(request))		

def google(request):
	print '--------------------------------> call google'
	
	data = {
		'DEBUG' : DEBUG,
	}

	return render_to_response('google4d6b20cf8373e41a.html', data, RequestContext(request))





# >>>>>>>>>>>>>>>>>>>>>>>>>>
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def jamuParse(request):
	print '--------------------------------> call jamuParse'
	html = "<html><body>It is now %s.</body></html>" % datetime.datetime.now()
	try:
		json_data = json.loads(request.body)
		if json_data['apikey'] == 'dasd122121kkjndsdas9898as8da':
			if json_data['trips_json'].__len__() > 0:
				for trip in json_data['trips_json']:
					date = datetime.datetime.strptime(trip['date'].encode('utf-8'), DEFAULT_DATETIME_FORMAT_JAMU)
					tripObject = Trip.objects.create_trip(date=date, 
		      								 type=str(trip['type'].encode('utf-8')), 
		      								 place_from=trip['place_from'], 
		      								 place_to=trip['place_to'], 
		      								 name=trip['name'], 
		      								 phone_number="+370"+trip['phone_number'], 
		      								 comments=trip['comments'])

	except KeyError:
		HttpResponseServerError("error in jamu data!")

	return HttpResponse(html)
