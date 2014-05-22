# coding=utf-8 

#cities
Cities_LT_FULL = (
	(u' Any', ['Visi']),
	(u'Airija', ['Airija']),
	(u'Anglija', ['Anglija']),
	(u'Baltarusija', ['Baltarusija']),
	(u'Belgija', ['Belgija']),
	(u'Čekija', ['Cekija']),
	(u'Danija', ['Danija']),
	(u'Estija', ['Estija']),
	(u'Ispanija', ['Ispanija']),
	(u'Italija', ['Italija']),
	(u'Latvija', ['Latvija']),
	(u'Lenkija', ['Lenkija']),
	(u'Lietuva', ['Lietuva']),
	(u'Norvegija', ['Norvegija']),
	(u'Norvegija', ['Norvegija']),
	(u'Olandija', ['Olandija']),
	(u'Portugalija', ['Portugalija']),
	(u'Prancūzija', ['Prancuzija']),
	(u'Rusija', ['Rusija']),
	(u'Serbija', ['Serbija']),
	(u'Suomija', ['Suomija']),
	(u'Švedija', ['Svedija']),
	(u'Ukraina', ['Ukraina']),
	(u'Vengrija', ['Vengrija']),
	(u'Vokietija', ['Vokietija']),
	(u'Akmenė', ['Akmene']),
	(u'Alytus', ['Alytus', 'Alytu']),
	(u'Anykščiai', ['Anyksciai']),
	(u'Ariogala', ['Ariogala']),
	(u'Baltoji', ['Baltoji']),
	(u'Birštonas', ['Birstonas']),
	(u'Biržai', ['Birzai']),
	(u'Daugai', ['Daugai']),
	(u'Druskininkai', ['Druskininkai']),
	(u'Dūkštas', ['Dukstas']),
	(u'Dusetos', ['Dusetos']),
	(u'Eišiškės', ['Eisiskes']),
	(u'Elektrėnai', ['Elektrenai']),
	(u'Ežerėlis', ['Ezerelis']),
	(u'Gargždai', ['Gargzdai']),
	(u'Garliava', ['Garliava']),
	(u'Gelgaudiškis', ['Gelgaudiskis']),
	(u'Grigiškės', ['Grigiskes']),
	(u'Ignalina', ['Ignalina']),
	(u'Ylakiai', ['Ylakiai']),
	(u'Jieznas', ['Jieznas']),
	(u'Jonava', ['Jonava']),
	(u'Joniškėlis', ['Joniskelis']),
	(u'Joniškis', ['Joniskis']),
	(u'Jurbarkas', ['Jurbarkas']),
	(u'Kaišiadorys', ['Kaisiadorys']),
	(u'Kalvarija', ['Kalvarija']),
	(u'Kaunas', ['Kaunas']),
	(u'Kavarskas', ['Kavarskas']),
	(u'Kazlų', ['Kazlu']),
	(u'Kėdainiai', ['Kedainiai']),
	(u'Kelmė', ['Kelme']),
	(u'Kybartai', ['Kybartai']),
	(u'Klaipėda', ['Klaipeda']),
	(u'Kretinga', ['Kretinga']),
	(u'K.', ['K.']),
	(u'Kupiškis', ['Kupiskis']),
	(u'Kuršėnai', ['Kursenai']),
	(u'Kvėdarna', ['Kvedarna']),
	(u'Lazdijai', ['Lazdijai']),
	(u'Lentvaris', ['Lentvaris']),
	(u'Linkuva', ['Linkuva']),
	(u'Marijampolė', ['Marijampole']),
	(u'Mažeikiai', ['Mazeikiai']),
	(u'Molėtai', ['Moletai']),
	(u'N.', ['N.']),
	(u'Nemenčinė', ['Nemencine']),
	(u'Neringa', ['Neringa']),
	(u'Nida', ['Nida']),
	(u'Obeliai', ['Obeliai']),
	(u'Pabradė', ['Pabrade']),
	(u'Pagėgiai', ['Pagegiai']),
	(u'Pakruojis', ['Pakruojis']),
	(u'Palanga', ['Palanga']),
	(u'Pandėlys', ['Pandelys']),
	(u'Panemunė', ['Panemune']),
	(u'Panevėžys', ['Panevezys']),
	(u'Pasvalys', ['Pasvalys']),
	(u'Plungė', ['Plunge']),
	(u'Priekulė', ['Priekule']),
	(u'Prienai', ['Prienai']),
	(u'Radviliškis', ['Radviliskis']),
	(u'Ramygala', ['Ramygala']),
	(u'Raseiniai', ['Raseiniai']),
	(u'Rietavas', ['Rietavas']),
	(u'Rokiškis', ['Rokiskis']),
	(u'Rumšiškės', ['Rumsiskes']),
	(u'Rūdiškės', ['Rudiskes']),
	(u'Salantai', ['Salantai']),
	(u'Seda', ['Seda']),
	(u'Simnas', ['Simnas']),
	(u'Skaudvilė', ['Skaudvile']),
	(u'Skuodas', ['Skuodas']),
	(u'Smalininkai', ['Smalininkai']),
	(u'Subačius', ['Subacius']),
	(u'Šakiai', ['Sakiai']),
	(u'Šalčininkai', ['Salcininkai']),
	(u'Šeduva', ['Seduva']),
	(u'Šiauliai', ['Siauliai']),
	(u'Šilalė', ['Silale']),
	(u'Šilutė', ['Silute']),
	(u'Širvintos', ['Sirvintos']),
	(u'Švenčionėliai', ['Svencioneliai']),
	(u'Švenčionys', ['Svencionys']),
	(u'Tauragė', ['Taurage']),
	(u'Telšiai', ['Telsiai']),
	(u'Tytuvėnai', ['Tytuvenai']),
	(u'Trakai', ['Trakai']),
	(u'Troškūnai', ['Troskunai']),
	(u'Ukmergė', ['Ukmerge']),
	(u'Utena', ['Utena', 'Utenos']),
	(u'Užventis', ['Uzventis']),
	(u'Vabalninkas', ['Vabalninkas']),
	(u'Varėna', ['Varena']),
	(u'Varniai', ['Varniai']),
	(u'Veisiejai', ['Veisiejai']),
	(u'Venta', ['Venta']),
	(u'Vėžaičiai', ['Vezaiciai']),
	(u'Viekšniai', ['Vieksniai']),
	(u'Vievis', ['Vievis']),
	(u'Vilkaviškis', ['Vilkaviskis']),
	(u'Vilkija', ['Vilkija']),
	(u'Vilnius', ['Vilnius', 'Vilniaus', 'Vilniu']),
	(u'Virbalis', ['Virbalis']),
	(u'Visaginas', ['Visaginas']),
	(u'Zarasai', ['Zarasai']),
	(u'Žagarė', ['Zagare']),
	(u'Žiežmariai', ['Ziezmariai']),
)

from collections import OrderedDict
not_sorted_dict = dict(tuple([(k,v[0].encode('utf-8')) for (k,v) in dict(Cities_LT_FULL).items()]))
sorted_dict = OrderedDict(sorted(not_sorted_dict.items(), key=lambda t: t[1]))
Cities_LT = tuple(list(sorted_dict.items()))

# Cities_LT = (
# (u' Any', 'Visi'), #DONT TUCH!!!
# (u'*Airija', '*Airija'),
# (u'*Anglija', '*Anglija'),
# (u'*Baltarusija', '*Baltarusija'),
# (u'*Belgija', '*Belgija'),
# (u'*Čekija', '*Čekija'),
# (u'*Danija', '*Danija'),
# (u'*Estija', '*Estija'),
# (u'*Ispanija', '*Ispanija'),
# (u'*Italija', '*Italija'),
# (u'*Latvija', '*Latvija'),
# (u'*Lenkija', '*Lenkija'),
# (u'*Lietuva', '*Lietuva'),
# (u'*Norvegija', '*Norvegija'),
# (u'*Norvegija', '*Norvegija'),
# (u'*Olandija', '*Olandija'),
# (u'*Portugalija', '*Portugalija'),
# (u'*Prancūzija', '*Prancūzija'),
# (u'*Rusija', '*Rusija'),
# (u'*Serbija', '*Serbija'),
# (u'*Suomija', '*Suomija'),
# (u'*Švedija', '*Švedija'),
# (u'*Ukraina', '*Ukraina'),
# (u'*Vengrija', '*Vengrija'),
# (u'*Vokietija', '*Vokietija'),
# (u'Akmenė', 'Akmenė'),
# (u'Alytus', 'Alytus'),
# (u'Anykščiai', u'Anykščiai'),
# (u'Ariogala', 'Ariogala'),
# (u'Baltoji Vokė', 'Baltoji Vokė'),
# (u'Birštonas', 'Birštonas'),
# (u'Biržai', 'Biržai'),
# (u'Daugai', 'Daugai'),
# (u'Druskininkai', 'Druskininkai'),
# (u'Dūkštas', 'Dūkštas'),
# (u'Dusetos', 'Dusetos'),
# (u'Eišiškės', 'Eišiškės'),
# (u'Elektrėnai', 'Elektrėnai'),
# (u'Ežerėlis', 'Ežerėlis'),
# (u'Gargždai', 'Gargždai'),
# (u'Garliava', 'Garliava'),
# (u'Gelgaudiškis', 'Gelgaudiškis'),
# (u'Grigiškės', 'Grigiškės'),
# (u'Ignalina', 'Ignalina'),
# (u'Ylakiai', 'Ylakiai'),
# (u'Jieznas', 'Jieznas'),
# (u'Jonava', 'Jonava'),
# (u'Joniškėlis', 'Joniškėlis'),
# (u'Joniškis', 'Joniškis'),
# (u'Jurbarkas', 'Jurbarkas'),
# (u'Kaišiadorys', 'Kaišiadorys'),
# (u'Kalvarija', 'Kalvarija'),
# (u'Kaunas', 'Kaunas'),
# (u'Kavarskas', 'Kavarskas'),
# (u'Kazlų Rūda', 'Kazlų Rūda'),
# (u'Kėdainiai', 'Kėdainiai'),
# (u'Kelmė', 'Kelmė'),
# (u'Kybartai', 'Kybartai'),
# (u'Klaipėda', 'Klaipėda'),
# (u'Kretinga', 'Kretinga'),
# (u'K. Naumiestis', 'K. Naumiestis'),
# (u'Kupiškis', 'Kupiškis'),
# (u'Kuršėnai', 'Kuršėnai'),
# (u'Kvėdarna', 'Kvėdarna'),
# (u'Lazdijai', 'Lazdijai'),
# (u'Lentvaris', 'Lentvaris'),
# (u'Linkuva', 'Linkuva'),
# (u'Marijampolė', 'Marijampolė'),
# (u'Mažeikiai', 'Mažeikiai'),
# (u'Molėtai', 'Molėtai'),
# (u'N. Akmenė', 'N. Akmenė'),
# (u'Nemenčinė', 'Nemenčinė'),
# (u'Neringa', 'Neringa'),
# (u'Nida', 'Nida'),
# (u'Obeliai', 'Obeliai'),
# (u'Pabradė', 'Pabradė'),
# (u'Pagėgiai', 'Pagėgiai'),
# (u'Pakruojis', 'Pakruojis'),
# (u'Palanga', 'Palanga'),
# (u'Pandėlys', 'Pandėlys'),
# (u'Panemunė', 'Panemunė'),
# (u'Panevėžys', 'Panevėžys'),
# (u'Pasvalys', 'Pasvalys'),
# (u'Plungė', 'Plungė'),
# (u'Priekulė', 'Priekulė'),
# (u'Prienai', 'Prienai'),
# (u'Radviliškis', 'Radviliškis'),
# (u'Ramygala', 'Ramygala'),
# (u'Raseiniai', 'Raseiniai'),
# (u'Rietavas', 'Rietavas'),
# (u'Rokiškis', 'Rokiškis'),
# (u'Rumšiškės', 'Rumšiškės'),
# (u'Rūdiškės', 'Rūdiškės'),
# (u'Salantai', 'Salantai'),
# (u'Seda', 'Seda'),
# (u'Simnas', 'Simnas'),
# (u'Skaudvilė', 'Skaudvilė'),
# (u'Skuodas', 'Skuodas'),
# (u'Smalininkai', 'Smalininkai'),
# (u'Subačius', 'Subačius'),
# (u'Šakiai', 'Šakiai'),
# (u'Šalčininkai', 'Šalčininkai'),
# (u'Šeduva', 'Šeduva'),
# (u'Šiauliai', 'Šiauliai'),
# (u'Šilalė', 'Šilalė'),
# (u'Šilutė', 'Šilutė'),
# (u'Širvintos', 'Širvintos'),
# (u'Švenčionėliai', 'Švenčionėliai'),
# (u'Švenčionys', 'Švenčionys'),
# (u'Tauragė', 'Tauragė'),
# (u'Telšiai', 'Telšiai'),
# (u'Tytuvėnai', 'Tytuvėnai'),
# (u'Trakai', 'Trakai'),
# (u'Troškūnai', 'Troškūnai'),
# (u'Ukmergė', 'Ukmergė'),
# (u'Utena', 'Utena'),
# (u'Užventis', 'Užventis'),
# (u'Vabalninkas', 'Vabalninkas'),
# (u'Varėna', 'Varėna'),
# (u'Varniai', 'Varniai'),
# (u'Veisiejai', 'Veisiejai'),
# (u'Venta', 'Venta'),
# (u'Vėžaičiai', 'Vėžaičiai'),
# (u'Viekšniai', 'Viekšniai'),
# (u'Vievis', 'Vievis'),
# (u'Vilkaviškis', 'Vilkaviškis'),
# (u'Vilkija', 'Vilkija'),
# (u'Vilnius', 'Vilnius'),
# (u'Virbalis', 'Virbalis'),
# (u'Visaginas', 'Visaginas'),
# (u'Zarasai', 'Zarasai'),
# (u'Žagarė', 'Žagarė'),
# (u'Žiežmariai', 'Žiežmariai'),
# )

#TriopType
TripType_RU = {
	(u'Any', 'Все'),  #DONT TUCH!!!
	(u'Driver', 'Водителей'),
	(u'Passenger', 'Пассажиров'),
}

TripType_LT = {
	(u'Any', 'Visi'),
    (u'Keleivis', 'Keleivis'),	
	(u'Driver', 'Vairuotojas'),
	
}

#controls
Controls_RU = {
	'Go': u'Поиск',
	'Add': u'+',
	'AddNewTrip': u'Добавить поездку',
	'Save': u'Сохранить',
	'Trips': u'Поездки',
	'From:': u'Откуда:',
	'To:': u'Куда:',
	'Type:': u'Ищу:',
	'Filters': u'Поиск поездок',
	'NewTrip': u'Новая поездка',
	'Trips': u'Поездки',
	'Save': u'Сохранить',
	'Delete': u'-',
	'ShowAllItems': u'Показать все записи',
	'AddNewTrip_Tooltip': u'Создать поездку',
	'Search_Tooltip': u'Начать поиск по фильтрам',
	'AddFilter_Tooltip': u'Добавить фильтр',
	'DeleteFilter_tooltip': u'Удалить фильтр',
	'Save_tooltip': u'Сохранить сообщение',
	'Trips_tooltip': u'Закрыть форму',
	'SiteName': u'Полная машина | Поиск попутчиков в Литве',
	'SiteDescription': u'Найди себе дружелюбную компанию. Быстрый и удобный способ путешествовать между городами Литвы и за границу.',
}

Controls_LT = {
	'Go': u'Ieškoti',
	'Add': u'+',
	'AddNewTrip': u'Sukurti',
	'Save': u'Išsaugoti',
	'Trips': u'Kelionės',
	'From:': u'Iš:',
	'To:': u'Į:',
	'When:': u'Kada:',
	'Where:': u'Kur:',
	'Type:': u'Ieškau:',
	'Filters': u'Kelionių paieška',
	'NewTrip': u'Nauja kelionė',
	'Trips': u'Kelionės',
	'Save': u'Išsaugoti',
	'Delete': u'-',
	'ShowAllItems': u'Rodyti visus įrašus',
	'AddNewTrip_Tooltip': u'Sukurti skelbimą',
	'Search_Tooltip': u'Pradėti paiešką',
	'AddFilter_Tooltip': u'Pridėti filtrą',
	'DeleteFilter_tooltip': u'Pašalinti filtrą',
	'Save_tooltip': u'Išsaugoti skelbimą',
	'Trips_tooltip': u'Uždaryti formą',
	'SiteName': u'Pilna mašina | Pakeleivių paieška Lietuvoje',
	'SiteDescription': u'Surask sau draugiską kompaniją. Greitas ir patogus būdas keliauti tarp Lietuvos miestų ir į užsienį.',
}

#new trip
#RUSSIAN
NewTrip_RU = {
	'name': '* Имя:',
	'place_from': '* Откуда:',
	'place_to': '* Куда:',
	'type': '* Роль:',
	'comments': 'Комментарий:',
	'phone_number': '* Телефон:',
	'date': '* Дата:',
	'captcha': '* Код безопасности:',
}

#LITHUANIAN
NewTrip_LT = {
	'name': '* Vardas:',
	'place_from': '* Iš:',
	'place_to': '* Į:',
	'type': '* Esu:',
	'comments': 'Komentaras:',
	'phone_number': '* Telefonas:',
	'date': '* Data:',
	'captcha': '* Apsaugos kodas:',
}

# time
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
	'dateFormat': u'yy.mm.dd',
	'pythonDateFormat': '%Y.%m.%d %H:%M',
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
	'currentText': u'Važiuočiau dabar',
	'closeText': u'Išsaugoti',
	'timeFormat': u'HH:mm',
	'amNames': ['AM', 'A'],
	'pmNames': ['PM', 'P'],
}

Date_LT = {
	'closeText': u'Uždaryti',
	'prevText': u'Ankst',
	'nextText': u'Sekan',
	'currentText': u'Šiandien',
	'monthNames': [u'Sausis',u'Vasaris',u'Kovas',u'Balandis',u'Gegužė',u'Birželis', u'Liepa',u'Rugpjūtis',u'Rugsėjis',u'Spalis',u'Lapkritis',u'Gruodis'],
	'monthNamesShort': [u'Sau',u'Vas',u'Kov',u'Bal',u'Geg',u'Bir',u'Lie',u'Rugp',u'Rugs',u'Spa',u'Lap',u'Gruo'],
	'dayNames': [u'sekmadienis',u'pirmadienis',u'antradienis',u'trečiadienis',u'ketvirtadienis',u'penktadienis',u'šeštadienis'],
	'dayNamesShort': [u'sekm',u'pirm',u'antr',u'treč',u'ketv',u'penk',u'šešt'],
	'dayNamesMin': [u'Sk',u'Pr',u'An',u'Tr',u'Kt',u'Pn',u'Še'],
	'weekHeader': u'Не',
	'dateFormat': u'yy.mm.dd',
	'pythonDateFormat': '%Y.%m.%d %H:%M',
}

# Validation
Validation_RU = {
	'empty_date' : u'Вы не можете ввести пустую дату', #u'You cannot input empty date'
	'less_current_date' : u'Вы не можете ввести дату меньше текущей', #u'You cannot input less then current date'
	'empty_place_from' : u'Вы должны ввести место отправления', #u'You must input place from to create new trip'
	'empty_place_to' : u'Вы должны ввести место прибытия', #u'You must input place to to create new trip'
	'empty_type' : u'Вы должны ввести тип участника',
	'empty_name' : u'Вы должны ввести имя', #u'You must input name to create new trip'
	'required' : u'Поле должно быть заполнено', #u'This field is required'
	'invalid' : u'Не правильный формат номера телефона', #u'This field is required'
	'captcha_invalid' : u'Не правильная капча', #u'This field is required'
}

Validation_LT = {
	'empty_date' : u'Kokia kelionės data?', #u'You cannot input empty date'
	'less_current_date' : u'Įveskite vėlesnį laiką', #u'You cannot input less then current date'
	'empty_place_from' : u'Iš kurio miesto išvykstate?', #u'You must input place from to create new trip'
	'empty_place_to' : u'Į kurį miestą vykstate?', #u'You must input place to to create new trip'
	'empty_type' : u'Koks dalyvio tipas?',
	'empty_name' : u'Koks dalyvio vardas?', #u'You must input name to create new trip'
	'required' : u'Laukas turi būti užpildytas', #u'This field is required'
	'invalid' : u'Neteisingas tel. numeris', #u'This field is required'
	'captcha_invalid' : u'Neteisingai įvęstas Captcha kodas', #u'This field is required'
	'invalid_phonenumber_length' : u'Не правильная длинна телефонного номера', #u'This field is required'
}

PhonePrefix_LT = '+3706'

#defaults
DEFAULT_PHONEPREFIX = PhonePrefix_LT
DEFAULT_TRIPTYPE = TripType_LT
DEFAULT_VALIDATION = Validation_LT 
DEFAULT_DATETIME_FORMAT_SERVER = '%Y.%m.%d %H:%M'
DEFAULT_DATETIME_FORMAT_CLIENT = '%m/%d/%Y %H:%M'
DEFAULT_DATETIME_FORMAT_DJANGO = 'YYYY-MM-DD HH:MM'
DEFAULT_DATETIME_FORMAT_JAMU = '%Y-%m-%d %H:%M:%S'
DEFAULT_CONTROLS = Controls_LT
DEFAULT_CITY = Cities_LT
DEFAULT_CITY_FULL = Cities_LT_FULL
DEFAULT_TIME = Time_LT
DEFAULT_DATE = Date_LT
DEFAULT_TRANSLATE_NEW_TRIP = NewTrip_LT
NEW_TRIP_SESSION_DURATION = 60*2
NEW_TRIP_COUNT = 3