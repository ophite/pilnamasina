# coding=utf-8
# -*- coding: utf-8 -*- 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import time
import datetime
import re
import codecs
import json

DEFAULT_ENCODING = 'utf-8'

# running service params
URL_DEBUG = 'http://127.0.0.1:8000/api/jamu/'
URL = 'http://http://pilnamasina.lt//api/jamu/'
URL_CURRENT = URL_DEBUG
SERVICE_SLEEP_TIME_DEBUG = 10 # 10 seconds
SERVICE_SLEEP_TIME = 60*30 # 30 minutes
SERVICE_SLEEP_TIME_CURRENT = SERVICE_SLEEP_TIME_DEBUG
SERVICE_MAX_RUNNING_COUNT = 1000


FILE_PARSER_SINGLE = "log\jamu_single.txt"
FILE_PARSER = "log\jamu.txt"
FILE_ARCHIVE = "log\jamu_archive.txt"
FILE_ERROR = "log\jamu_error.txt"
FILE_GOOD = "log\jamu_good.txt"
FILE_BAD = "log\jamu_bad.txt"


DAYS = {
		"Monday": [],
		"Tuesday": [],
		"Wednesday": [],
		"Thursday": [u'Ketvirtadienį'],
		"Friday": [u"Penktadienį", u'Penktadienis', u'Penktadieni'],
		"Saturday": [u"Sestadieni"],
		"Sunday": [],
		}


def parse():
	driver = webdriver.Firefox()
	driver.get("http://jamu.lt/")

	try:
		# 1 jamu
		time_sleep_duration = 2
		element = WebDriverWait(driver, 10).until(
			expected_conditions.presence_of_element_located((By.CLASS_NAME, "text"))
		)
		time.sleep(time_sleep_duration)
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(time_sleep_duration)
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(time_sleep_duration)
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		items = driver.find_elements_by_class_name("text")
		# 2 restart (not found sometimes)
		if items.__len__() == 0 or items.__len__() == 1:
		    driver.quit()
		    driver = None
		    parse()
		# 3 write to file
		trips = []
		for item in driver.find_elements_by_class_name("text"):
			parent = driver.execute_script("return arguments[0].parentNode.parentNode;", item)
			a = parent.find_element_by_tag_name('a')
			trip = TripObject()
			trip.name = a.text.encode(DEFAULT_ENCODING)
			trip.comments = item.text.encode(DEFAULT_ENCODING)
			trips.append(trip)
		# json, file
		if trips.__len__() == 0:
			print "Message during parsing. No trip parsed"
			return

		text_file = codecs.open(FILE_PARSER, mode = "w", encoding = DEFAULT_ENCODING)
		trips_json = json.dumps(trips, ensure_ascii = False, cls = TripObjectEncoder)
		json.dump(trips_json.decode(DEFAULT_ENCODING), text_file, ensure_ascii = False, encoding = DEFAULT_ENCODING)
	except Exception, error:
		writeToFileError(trip = None, error = error)
		print "Error during parsing:{0}".format(error)
	finally:
		if driver != None:
			driver.quit()
			driver = None
		if text_file != None:
			text_file.close()



class MetaTripObject(type):
    def __str__(self):
        return "Klass"


class TripObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, TripObject):
            return obj.get_json_state()
        else:
            return json.JSONEncoder.default(self, obj)


class TripObject(object):
	__metaclass__ = MetaTripObject

	date = None
	type = ''
	place_from = ''
	place_to = ''
	name = ''
	phone_number = ''
	comments = ''
	# additional field for checking already parsed messages
	dateArchive = None

	"""docstring for TripObject"""
	def __init__(self):
		super(TripObject, self).__init__()

	def strForBadTrip(self):
		return "place_from:{0} place_to:{1} dateArchive:{2} phone_number:{3} name:{4} type:{5} comments:{6}".format(self.place_from, self.place_to, self.dateArchive, self.phone_number, self.name, self.type, self.comments)

	def __str__(self):
		return "place_from:{0} place_to:{1} date:{2} phone_number:{3} name:{4} type:{5} comments:{6}".format(self.place_from, self.place_to, str(self.date), self.phone_number, self.name, self.type, self.comments)

	def get_json_state(self):
		return {
				"date":str(self.date), 
				"type":self.type, 
				"place_from":self.place_from, 
				"place_to":self.place_to, 
				"name":self.name, 
				"phone_number":self.phone_number, 
				"comments":self.comments, 
				"dateArchive":str(self.dateArchive)
				}


#1(Day)  Если есть **.** либо **-**      - это день
#2(Time) Если есть **:**, **-**        - это часы, в вдругом случае подставлять 00:00
#3(From-To) Если есть слово-слово            - это откуда-куда (берем только первые два слова)
#3(From-To) Если есть слово->слово            - это откуда-куда (берем только первые два слова)
#4(Phone) Если есть длинное число - это номер телефона (нужно сделать "Телефон" не обязательным полем, 
#5(photo, name, fb link) т.к. у нас появяться ссылки на людей в ФБ и телефон уже не супер обязателен)
	
def dictToTrip(dict):
	l = lambda d, key: (d[key].encode(DEFAULT_ENCODING) if d[key] != None else None) if d.has_key(key) else None
	trip = TripObject()
	trip.date = l(dict, u'date')
	trip.type = l(dict, u'type')
	trip.place_from = l(dict, u'place_from')
	trip.place_to = l(dict, u'place_to')
	trip.name = l(dict, u'name')
	trip.phone_number = l(dict, u'phone_number')
	trip.comments = l(dict, u'comments')
	trip.dateArchive = l(dict, u'dateArchive')
	return trip


def readFromFile():
	# >>>>>>>>>> 0 PREPARE
	# import from localize
	import os, sys
	currDir =  os.path.dirname(os.path.abspath(__file__))
	currDir = currDir[:currDir.rindex("\\")]
	currDir = currDir[:currDir.rindex("\\")]
	sys.path.insert(0, currDir)
	from myapp.translate.localize import DEFAULT_CITY_FULL 

	#open file
	# json
	trips = []
	trips_json = []
	trips_good = []
	trips_bad = []
	# >>>>>>>>>> 1 READ DATA
	with codecs.open(FILE_PARSER, mode = "r", encoding = DEFAULT_ENCODING) as f:
	# with codecs.open(FILE_PARSER_SINGLE, mode = "r", encoding = DEFAULT_ENCODING) as f:
		for line in f:
			trips_json.append(json.loads(line))

	trips_json = json.loads(trips_json[0], encoding = DEFAULT_ENCODING)
	for trip_json in trips_json:
		trip = dictToTrip(trip_json)
		trips.append(trip)

	# read bad trips
	text_file = codecs.open(FILE_BAD, mode = "r", encoding = DEFAULT_ENCODING)
	trips_bad_archive = []
	[trips_bad_archive.append(item.encode(DEFAULT_ENCODING).strip()) for item in text_file]
	text_file.close()
	# read archive trips
	text_file = codecs.open(FILE_ARCHIVE, mode = "r", encoding = DEFAULT_ENCODING)
	trips_good_archive = []
	[trips_good_archive.append(item.encode(DEFAULT_ENCODING).strip()) for item in text_file]
	text_file.close()

	# >>>>>>>>>> 2 PARSING
	for trip in trips:
		try:
			trip_original = trip
			# >>>>>>>>>>>>>>>>>>>> Day
			if trip.comments.decode(DEFAULT_ENCODING).lower().encode(DEFAULT_ENCODING).__contains__(u"Šiandien".lower().encode(DEFAULT_ENCODING)):
				today = datetime.datetime.today() # datetime.timedelta(N)
				trip.date = datetime.datetime(today.year, today.month, today.day)
			if trip.comments.decode(DEFAULT_ENCODING).lower().encode(DEFAULT_ENCODING).__contains__(u"Rytoj".lower().encode(DEFAULT_ENCODING)):
				today = datetime.datetime.today() # datetime.timedelta(N)
				trip.date = datetime.datetime(today.year, today.month, today.day) + datetime.timedelta(1)

			# by week day name (monday, friday .. )
			for day, lt_days in DAYS.items():
				for lt_day in lt_days:
					if trip.comments.decode(DEFAULT_ENCODING).lower().encode(DEFAULT_ENCODING).__contains__(lt_day.lower().encode(DEFAULT_ENCODING)):
						today = datetime.datetime.today() # datetime.timedelta(N)
						dayNumber = weekDay(today.year, today.month, today.day)[0]
						dayNumber_lt = weekDayNumber(day)
						if dayNumber_lt > dayNumber:
							trip.date = datetime.datetime(today.year, today.month, today.day) + datetime.timedelta(dayNumber_lt - dayNumber)

			if trip.date == None or trip.date == 'None':
				DAY_RE_TEMPLATE_LIST = (
										r'(\d{4})[/.-](\d{2})[/.-](\d{2})', 	# 2014.05.14
										r'(\D{1}(?!.)\d{2})[.](\d{2})', 		# 05.14
										r'(\s\d{2})[.](\d{2})(?!val)', 			# 05.14	NOT "val"
										r'(\s\d{2})[.](\d{2})(\s?!val)', 		# 05.14 NOT " val"
										)
				for re_template in DAY_RE_TEMPLATE_LIST:
					reg = re.compile(re_template)
					gr = reg.search(trip.comments)
					if gr == None:
						continue

					gr = gr.groups()
					if gr.__len__() == 3:
						trip.date = datetime.date(int(gr[0]), int(gr[1]), int(gr[2]))
					if gr.__len__() == 2:
						if (int(gr[0])) > 12:
							continue
						if (int(gr[0])) > 31:
							continue
						trip.date = datetime.date(datetime.datetime.today().year, int(gr[0]), int(gr[1]))
						break
			# >>>>>>>>>>>>>>>>>>>> Time
			TIME_RE_TEMPLATE_LIST = (
									r'(\d{2}[/.,-:]\d{2})[/-](\d{2}[/.,-:]\d{2})',	# 15.30-16.30
									r'(\d{2})[/-](\d{2}[/.,-:]\d{2})',				# 15-16.30
									r'(\d{2}[/.,-:]\d{2})[/-](\d{2})',				# 15.30-16
									r'(\d{1,2})[-.,](\d{2}valanda)',				# 15-30valanda
									r'(\d{1,2})[-.,](\d{2} valanda)',				# 15-30 valanda
									r'(\d{1,2})[:.,](\d{2}valanda)',				# 15:30valanda
									r'(\d{1,2})[:.,](\d{2} valanda)',				# 15:30 val
									r'(\d{1,2})[-.,](\d{2}val)',					# 15-16val
									r'(\d{1,2})[-.,](\d{2} val)',					# 15-16 val
									r'(\d{1,2})[:.,](\d{2}val)',					# 15:16val
									r'(\d{1,2})[:.,](\d{2} val)',					# 15:30 val
									r'(\d{1,2})[:](\d{2})',							# 15:30
									r'(~\d{1,2})[-:.,](\d{2})',						# 15:30
									r'(\d{1,2})[:.,](\d{2}h)',						# 15:30h
									r'(\d{1,2})[-.,](\d{2}h)',						# 15-16h
									r'( \d{1,2}h)',									# 15h
									r'( \d{1,2}val)',								# 15val
									r'( \d{1,2} val)',								# 15 val
									r'(~\d{1,2}val)',								# ~15val
									r'(~\d{1,2} val)',								# ~15val
									r'(~\d{1,2} valanda)',							# ~15 valanda
									r'(~\d{1,2}valanda)',							# ~15valanda
									r'( \d{1,2} valanda)',							# 15 valanda
									r'( \d{1,2}valanda)',							# 15valanda
								   )
			for re_template in TIME_RE_TEMPLATE_LIST:
				reg = re.compile(re_template)
				gr = reg.search(trip.comments) #
				if gr != None:
					gr = gr.groups()
					if gr.__len__() == 0:
						continue

					time = gr[0].replace(' ', '').replace('valanda', '').replace('val', '').replace('h', '')
					if re_template == r'(\d{2}[/.,-:]\d{2})[/-](\d{2}[/.,-:]\d{2})':
						if time.__contains__(':'):
							hour = time.split(':')[0] 
						elif time.__contains__('.'):
						 	hour = time.split('.')[0]
						elif time.__contains__(','):
						 	hour = time.split(',')[0]
						elif time.__contains__('-'):
						 	hour = time.split('-')[0]
						if time.__contains__(':'):
							minute = time.split(':')[1] 
						elif time.__contains__('.'):
						 	minute = time.split('.')[1]
						elif time.__contains__(','):
						 	minute = time.split(',')[1]
						elif time.__contains__('-'):
						 	minute = time.split('-')[1]
					elif re_template == r'(\d{2})[/-](\d{2}[/.,-:]\d{2})':
						if time.__contains__(':'):
							hour = time.split(':')[0] 
						elif time.__contains__('.'):
						 	hour = time.split('.')[0]
						elif time.__contains__(','):
						 	hour = time.split(',')[0]
						elif time.__contains__('-'):
						 	hour = time.split('-')[0]
						if time.__contains__(':'):
							minute = time.split(':')[1] 
						elif time.__contains__('.'):
						 	minute = time.split('.')[1]
						elif time.__contains__(','):
						 	minute = time.split(',')[1]
						elif time.__contains__('-'):
						 	minute = time.split('-')[1]
					elif re_template == r'(\d{2}[/.,-:]\d{2})[/-](\d{2})':
						if time.__contains__(':'):
							hour = time.split(':')[0] 
						elif time.__contains__('.'):
						 	hour = time.split('.')[0]
						elif time.__contains__(','):
						 	hour = time.split(',')[0]
						elif time.__contains__('-'):
						 	hour = time.split('-')[0]
						if time.__contains__(':'):
							minute = time.split(':')[1] 
						elif time.__contains__('.'):
						 	minute = time.split('.')[1]
						elif time.__contains__(','):
						 	minute = time.split(',')[1]
						elif time.__contains__('-'):
						 	minute = time.split('-')[1]
					else:
	
						if re_template.__contains__('~'):
							time = time.replace('~', '')
							hour = time
							if gr.__len__() > 1:
								minute = gr[1].replace(' ', '').replace('valanda', '').replace('val', '').replace('h', '')
							else:
								minute = 0
						elif re_template.__contains__('-'):
							hour = time
							minute = 0
						elif re_template.__contains__(':') or re_template.__contains__('.'):
							hour = time
							if gr.__len__() > 1:
								minute = gr[1].replace(' ', '').replace('valanda', '').replace('val', '').replace('h', '')
							else:
								minute = 0
						elif time.isdigit():
							hour = time
							minute = 0
						else:
							continue

					if trip.date == None or trip.date == 'None':
						today = datetime.datetime.today()
						trip.date = datetime.datetime(today.year, today.month, today.day)

					trip.date = datetime.datetime(trip.date.year, trip.date.month, trip.date.day, int(hour), int(minute))
					break
			# >>>>>>>>>>>>>>>>>>>> Phone
			reg = re.compile(r'(\d{9,})')
			gr = reg.search(trip.comments.replace(' ', '').replace('-', ''))
			if gr != None:
				gr = gr.groups()
				if gr.__len__() > 0:
					if gr[0].__len__() > 9:
						trip.phone_number = gr[0][gr[0].__len__() - 9:gr[0].__len__()]
					else:
						trip.phone_number = gr[0]
			else:
				continue
			# >>>>>>>>>>>>>>>>>>>> From-To
			FROMTO_SEPARATOR_LIST = (u" - ", u"-", u"- ", u" -", u" -> ", u"->", u" -- ", u" --> ", u"--", u"-->", 
									u"- į ", u" į ", u" i ", u"- i ")
			FROMTO_RE_TEMPLATE_LIST = (
										ur'([^\W\d_]+){0}([^\W\d_]+){1}([^\W\d_]+)',  		# KAUNAS - KLAIPEDA - PALANGA
									   	ur'([^\W\d_]+){0}(\([^\W\d_]+\)){1}([^\W\d_]+)',  	# KAUNAS - (KLAIPEDA) - PALANGA
									   	ur'([^\W\d_]+){0}([^\W\d_]+)'						# Klaipėda - Vilnius
									  )					
			city_dict = dict(DEFAULT_CITY_FULL)
			city_dict_full = {}
			for (key,values) in city_dict.items():
				value = [key.lower().encode(DEFAULT_ENCODING)] + [value.lower() for value in values]
				city_dict_full[values[0].encode(DEFAULT_ENCODING)] = value

			for re_template in FROMTO_RE_TEMPLATE_LIST:
				for separator in FROMTO_SEPARATOR_LIST:
					list_fromTo = re.search(re_template.format(separator, separator), trip.comments.strip().decode(DEFAULT_ENCODING), re.UNICODE)
					if list_fromTo == None or list_fromTo.groups().__len__ == 0:
						continue

					place_from = list_fromTo.groups()[0]
					if list_fromTo.groups().__len__() < 3:
						place_to = list_fromTo.groups()[1]  
					else:
						if list_fromTo.groups()[2] == list_fromTo.groups()[0]: 	# Mažeikiai-Klaipėda-Mažeikiai
							place_to = list_fromTo.groups()[1]  
						else:
							place_to = list_fromTo.groups()[2]

					if re.search(r'(\d{1})', place_from) != None or re.search(r'(\d{1})', place_to):
						continue

					place_from = place_from.lower().encode(DEFAULT_ENCODING)
					place_to = place_to.lower().encode(DEFAULT_ENCODING)

					for (key,values) in city_dict_full.items():
						if values.__contains__(place_from):
							trip.place_from = key
						if values.__contains__(place_to):
							trip.place_to = key
				if trip.place_from != '' or trip.place_to != '':
					break;
			# >>>>>>>>>>>>>>>>>>>> Defaults
			# if trip.date == None:
			# 	trip.date = datetime.datetime.today()
			trip.type = u'Keleivis'.encode(DEFAULT_ENCODING) # passanger

			# saving 
			date = datetime.datetime(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day) if trip.date == None or trip.date == 'None' else trip.date
			trip.dateArchive = datetime.datetime(int(date.year), int(date.month), int(date.day))

			if trips_bad_archive.__contains__(trip.strForBadTrip().strip()):
				continue
			if trips_good_archive.__contains__(str(trip).strip()):
				continue

			if trip.date == None or trip.date == 'None' or trip.place_from == '' or trip.place_to == '' or trip.phone_number == '' or trip.name == '':
				trips_bad.append(trip)
			else:
				trips_good.append(trip)
				trips_good_archive.append(trip)
			# only first trip
			# break
		except Exception, error:
			writeToFileError(trip, error)
			continue
	# >>>>>>>>>> 3 SAVE IN FILE
	# good new
	try:
		text_file = codecs.open(FILE_GOOD, mode = "w", encoding = DEFAULT_ENCODING)
		trips_json = json.dumps(trips_good, ensure_ascii = False, cls=TripObjectEncoder)
		json.dump(trips_json.decode(DEFAULT_ENCODING), text_file, ensure_ascii = False, encoding=DEFAULT_ENCODING)
	finally:
		text_file.close()
	# bad archive
	text_file = open(FILE_BAD, "a")
	try:
		for trip in trips_bad:
			text_file.write(trip.strForBadTrip())
			text_file.write('\n')
	finally:
		text_file.close()
	# good archive
	text_file = open(FILE_ARCHIVE, "a")
	try:
		for trip in trips_good:
			text_file.write(str(trip))
			text_file.write('\n')
	finally:
		text_file.close()
	# >>>>>>>>>> 4 SEND DATA 
	sendData()



def writeToFileError(trip, error):
	text_file = codecs.open(FILE_ERROR, mode = "a", encoding = DEFAULT_ENCODING)
	text_file.write("error:{0}".format(error))
	text_file.write('\n')
	print trip
	text_file.write(str(trip) if trip != None else ' no trip object ')
	text_file.write('\n')
	text_file.write('>>>>>>>>>>>>>>>>>>>>>>>>>')
	print "Error during trip.date = datetime:{0} comments:{1}".format(error, trip.comments)



def writeToFileDebug(str):
	FILE_DEBUG = "log\debug.txt"
	text_file = open(FILE_DEBUG, "w")
	try:
		text_file.write(str)
	finally:
		text_file.close()



def sendData():
	import json
	import requests
	from requests import ConnectionError
	trips_json = []
	with codecs.open(FILE_GOOD, mode = "r", encoding = DEFAULT_ENCODING) as f:
		for line in f:
			trips_json.append(json.loads(line))

	trips_json = json.loads(trips_json[0], encoding = DEFAULT_ENCODING)
	# print trips_json
	json_data = {'trips_json': trips_json, 'apikey': 'dasd122121kkjndsdas9898as8da'}
	json_data = json.dumps(json_data)
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	try:
		rensponse = requests.post(URL_CURRENT, data=json_data, headers=headers)
		print rensponse
	except ConnectionError, error:
		print 'ERROR: Server not response (start test server (127.0.0.1:8000) or check http://pilnamasina.lt/'




def weekDay(year, month, day):
    offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    week   = [
    			'Sunday', 
				'Monday', 
				'Tuesday', 
				'Wednesday', 
				'Thursday',  
				'Friday', 
				'Saturday'
			 ]
    afterFeb = 1
    if month > 2: afterFeb = 0
    aux = year - 1700 - afterFeb
    # dayOfWeek for 1700/1/1 = 5, Friday
    dayOfWeek  = 5
    # partial sum of days betweem current date and 1700/1/1
    dayOfWeek += (aux + afterFeb) * 365                  
    # leap year correction    
    dayOfWeek += aux / 4 - aux / 100 + (aux + 100) / 400     
    # sum monthly and day offsets
    dayOfWeek += offset[month - 1] + (day - 1)               
    dayOfWeek %= 7
    return dayOfWeek, week[dayOfWeek]



def weekDayNumber(name):
	week = {
			'Sunday':7, 
			'Monday':1, 
            'Tuesday':2, 
            'Wednesday':3, 
            'Thursday':4,  
            'Friday':5, 
            'Saturday':6,
            }
	return week[name]



def start():
	running_count = 0

	while True:
		print 'run parse'
		parse()
		print 'read from file'
		readFromFile()
		print 'sleep'
		time.sleep(SERVICE_SLEEP_TIME_CURRENT) 
		running_count = running_count + 1
		print 'parser running:{0} times'.format(running_count)
		if running_count == SERVICE_MAX_RUNNING_COUNT:
			break
	print 'finished'



#entry point
readFromFile()
# start()