# coding=utf-8 

#cities
Cities_LT = (
	('Visagines', 'Visagines') ,
	('Draunas', 'Draunas'),
	('Kaunas', 'Kaunas'),
	('Vilnus', 'Vilnus'),
)

#new trip translates
NewTrip_RU = (
	('name', 'Имя:') ,
	('place_from', 'Откуда:'),
	('place_to', 'Куда:'),
	('comments', 'Комментарий:'),
	('phone_number', 'Телефон:'),
	('date', 'Дата:'),
	('captcha', ' '),
)

NewTrip_LT = (
	('name', 'Имя:') ,
	('place_from', 'Откуда:'),
	('place_to', 'Куда:'),
	('comments', 'Комментарий:'),
	('phone_number', 'Телефон:'),
	('date', 'Дата:'),
	('captcha', ' '),
)

# time translates
Time_RU = {
	'timeOnlyTitle': u'Выберите время',
	'timeText': u'Время',
	'hourText': u'Часы',
	'minuteText': u'Минуты',
	'secondText': u'Секунды',
	'millisecText': u'Миллисекунды',
	'timezoneText': u'Часовой пояс',
	'currentText': u'Сейчас',
	'closeText': u'Закрыть',
	'timeFormat': u'HH:mm',
	'amNames': ['AM', 'A'],
	'pmNames': ['PM', 'P'],
}

Date_RU = {
	'closeText': u'Закрыть',
	'prevText': u'<Пред',
	'nextText': u'След>',
	'currentText': u'Сегодня',
	'monthNames': [u'Январь',u'Февраль',u'Март',u'Апрель',u'Май',u'Июнь', u'Июль',u'Август',u'Сентябрь',u'Октябрь',u'Ноябрь',u'Декабрь'],
	'monthNamesShort': [u'Янв',u'Фев',u'Мар',u'Апр',u'Май',u'Июн',u'Июл',u'Авг',u'Сен',u'Окт',u'Ноя',u'Дек'],
	'dayNames': [u'воскресенье',u'понедельник',u'вторник',u'среда',u'четверг',u'пятница',u'суббота'],
	'dayNamesShort': [u'вск',u'пнд',u'втр',u'срд',u'чтв',u'птн',u'сбт'],
	'dayNamesMin': [u'Вс',u'Пн',u'Вт',u'Ср',u'Чт',u'Пт',u'Сб'],
	'weekHeader': u'Не',
	'dateFormat': u'dd.mm.yy',
}
Time_LT = {
	'timeOnlyTitle': u'Выберите время',
	'timeText': u'Время',
	'hourText': u'Часы',
	'minuteText': u'Минуты',
	'secondText': u'Секунды',
	'millisecText': u'Миллисекунды',
	'timezoneText': u'Часовой пояс',
	'currentText': u'Сейчас',
	'closeText': u'Закрыть',
	'timeFormat': u'HH:mm',
	'amNames': ['AM', 'A'],
	'pmNames': ['PM', 'P'],
}

Date_LT = {
	'closeText': u'Закрыть',
	'prevText': u'<Пред',
	'nextText': u'След>',
	'currentText': u'Сегодня',
	'monthNames': [u'Январь',u'Февраль',u'Март',u'Апрель',u'Май',u'Июнь', u'Июль',u'Август',u'Сентябрь',u'Октябрь',u'Ноябрь',u'Декабрь'],
	'monthNamesShort': [u'Янв',u'Фев',u'Мар',u'Апр',u'Май',u'Июн',u'Июл',u'Авг',u'Сен',u'Окт',u'Ноя',u'Дек'],
	'dayNames': [u'воскресенье',u'понедельник',u'вторник',u'среда',u'четверг',u'пятница',u'суббота'],
	'dayNamesShort': [u'вск',u'пнд',u'втр',u'срд',u'чтв',u'птн',u'сбт'],
	'dayNamesMin': [u'Вс',u'Пн',u'Вт',u'Ср',u'Чт',u'Пт',u'Сб'],
	'weekHeader': u'Не',
	'dateFormat': u'dd.mm.yy',
}
#defaults
DEFAULT_CITY = Cities_LT
DEFAULT_TIME = Time_LT
DEFAULT_DATE = Date_LT
DEFAULT_TRANSLATE_NEW_TRIP = NewTrip_LT