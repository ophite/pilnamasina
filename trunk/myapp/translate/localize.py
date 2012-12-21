# coding=utf-8 

#cities
Cities_LT = (
	('Visagines', 'Visagines') ,
	('Draunas', 'Draunas'),
	('Kaunas', 'Kaunas'),
	('Vilnus', 'Vilnus'),
)

#controls
Controls_RU = {
	'Go': u'Поиск',
	'Add': u'Добавить',
	'AddNewTrip': u'Добавить поездку',
	'Save': u'Сохранить',
	'Trips': u'Поездки',
	'From:': u'Откуда:',
	'To:': u'Куда:',
	'Filters': u'Фильтры',
	'NewTrip': u'Новая поездка',
	'Trips': u'Поездки',
	'Save': u'Сохранить',
}

Controls_LT = {
	'Go': u'Поиск',
	'Add': u'Добавить',
	'AddNewTrip': u'Добавить поездку',
	'Save': u'Сохранить',
	'Trips': u'Поездки',
	'From:': u'Откуда:',
	'To:': u'Куда:',
	'Filters': u'Фильтры',
	'NewTrip': u'Новая поездка',
	'Trips': u'Поездки',
	'Save': u'Сохранить',
}

#new trip translates
#RUSSIAN
NewTrip_RU = (
	('name', 'Имя:') ,
	('place_from', 'Откуда:'),
	('place_to', 'Куда:'),
	('comments', 'Комментарий:'),
	('phone_number', 'Телефон:'),
	('date', 'Дата:'),
	('captcha', ' '),
)
#LITHUANIAN
NewTrip_LT = (
	('name', 'Vardas:') ,
	('place_from', 'Iš:'),
	('place_to', 'Į:'),
	('comments', 'Komentaras:'),
	('phone_number', 'Telefonas:'),
	('date', 'Data:'),
	('captcha', ' '),
)

# time translates
# RUSSIAN
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
	'pythonDateFormat': '%d.%m.%Y %H:%M',
}
# LITHUANIAN
Time_LT = {
	'timeOnlyTitle': u'Pasirinkite laiką',
	'timeText': u'Laikas',
	'hourText': u'Valandos',
	'minuteText': u'Minutės',
	'secondText': u'Sekundės',
	'millisecText': u'Milisekundės',
	'timezoneText': u'Laiko juosta',
	'currentText': u'Dabar',
	'closeText': u'Uždaryti',
	'timeFormat': u'HH:mm',
	'amNames': ['AM', 'A'],
	'pmNames': ['PM', 'P'],
}

Date_LT = {
	'closeText': u'Uždaryti',
	'prevText': u'<Ankst',
	'nextText': u'Sekan>',
	'currentText': u'Šiandien',
	'monthNames': [u'Sausis',u'Vasaris',u'Kovas',u'Balandis',u'Gegužė',u'Birželis', u'Liepa',u'Rugpjūtis',u'Rugsėjis',u'Spalis',u'Lapkritis',u'Gruodis'],
	'monthNamesShort': [u'Sau',u'Vas',u'Kov',u'Bal',u'Geg',u'Bir',u'Lie',u'Rugp',u'Rugs',u'Spa',u'Lap',u'Gruo'],
	'dayNames': [u'sekmadienis',u'pirmadienis',u'antradienis',u'trečiadienis',u'ketvirtadienis',u'penktadienis',u'šeštadienis'],
	'dayNamesShort': [u'sekm',u'pirm',u'antr',u'treč',u'ketv',u'penk',u'šešt'],
	'dayNamesMin': [u'Sk',u'Pr',u'An',u'Tr',u'Kt',u'Pn',u'Še'],
	'weekHeader': u'Не',
	'dateFormat': u'dd.mm.yy',
	'pythonDateFormat': '%d.%m.%Y %H:%M',
}

#defaults
DEFAULT_CONTROLS = Controls_LT
DEFAULT_CITY = Cities_LT
DEFAULT_TIME = Time_LT
DEFAULT_DATE = Date_LT
DEFAULT_TRANSLATE_NEW_TRIP = NewTrip_LT