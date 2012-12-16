from django.shortcuts import render_to_response
from django.template import loader, Context, RequestContext
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.utils import simplejson as json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

from myapp.models import Trip, LithuaniaCities
from myapp.forms import TripForm

import datetime
from datetime import date, timedelta

def add(request):
	print 'call add'

	if request.method == 'POST':
		form = TripForm(request.POST)
		
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/index/')
	else:
		form = TripForm()
	
	return render_to_response('add.html', {'form':form}, RequestContext(request))

def set_session(request):
	print 'call set_session'
	
	request.session['startdate'] = datetime.datetime.strptime(request.GET['startdate'], '%m/%d/%Y %H:%M')
	request.session['enddate'] = datetime.datetime.strptime(request.GET['enddate'], '%m/%d/%Y %H:%M')
	request.session['place_from'] = request.GET.get('place_from', '')
	request.session['place_to'] = request.GET.get('place_to', '')
	
	return render_to_response('add.html', RequestContext(request))

def index(request):
	print 'call index'
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
	LithuaniaCities_dict = dict(LithuaniaCities); 

	data = {
		'trips':trips, 
		'startdate':startdate.strftime('%Y-%m-%dT%H:%M:%S'),
		'enddate':enddate.strftime('%Y-%m-%dT%H:%M:%S'),
		'place_from':place_from,
		'place_to':place_to,
		'cities':LithuaniaCities_dict,
	}

	return render_to_response('index.html', data, RequestContext(request))

def search(request):
	print 22222
	
	startdate = datetime.datetime.strptime(request.GET['date_from'], '%m/%d/%Y %H:%M')
	enddate = datetime.datetime.strptime(request.GET['date_to'], '%m/%d/%Y %H:%M')
	
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
