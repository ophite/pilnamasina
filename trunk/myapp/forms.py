# coding=utf-8
from django import forms
from django.core import validators
from django.forms import ModelForm, Textarea
from django.forms.util import ErrorList
from django.utils.timezone import utc
from django.utils import timezone
 
#python
import datetime
#my
from myapp.models import Trip
from myapp.translate.localize import *
#3rd party
from recaptchawidget.fields import ReCaptchaField 

"""
from django.forms.widgets import Widget
from __future__ import unicode_literals
Работает и без этого
def flatatt(attrs):
    return u''.join([u' %s="%s"' % (k, conditional_escape(v)) for k, v in attrs.items()])
	
class Label(Widget):    
    def render(self, name, value, attrs=None):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
       return mark_safe(u'<label%s>%s</label>' % (flatatt(final_attrs),
                conditional_escape(force_unicode(value))))
"""

jquery_input_class = 'ui-combobox-input ui-state-default ui-widget ui-widget-content ui-corner-left ui-corner-right'
jquery_combo_class = 'ui-combobox-input ui-state-default ui-widget ui-widget-content'

class DivModelForm(forms.ModelForm):
    error_css_class = 'class-error'
    #required_css_class = 'class-required'
    def as_div(self):
        return self._html_output(
            normal_row = u'<div%(html_class_attr)s>%(label)s %(field)s %(help_text)s %(errors)s</div>',
            #error_row = u'<div class="error">%s</div>',
			error_row = u'%s',
            row_ender = '</div>',
            help_text_html = u'<div class="hefp-text">%s</div>',
            errors_on_separate_row = False)

class TripForm(forms.ModelForm): #DivModelForm
	# captcha = ReCaptchaField()
	date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class':jquery_input_class}, format = DEFAULT_DATETIME_FORMAT_SERVER), input_formats=(DEFAULT_DATETIME_FORMAT_SERVER,))

	def __init__(self, *args, **kwargs):
		print '--------------------------------> call __init__ TripForm'

		self.request = kwargs.pop('request', None)
		super(TripForm, self).__init__(*args, **kwargs)
		self.label_suffix = ''
		d = DEFAULT_TRANSLATE_NEW_TRIP
				
		for name, field in self.fields.items():
			print name, field
			#localize label
			field.label = field.label if d.get(name) is None else d[name]
			#localize error msg
			for k,v in field.error_messages.items():
				field.error_messages[k] = DEFAULT_VALIDATION.get(k, v)
				
			if field.widget.__class__ == forms.widgets.Textarea:
				if field.widget.attrs.has_key('class'):
					field.widget.attrs['class'] += ' ' + jquery_input_class
				else:
					field.widget.attrs.update({'class':jquery_input_class})
			
			if field.widget.__class__ == forms.widgets.TextInput:
				if field.widget.attrs.has_key('class'):
					field.widget.attrs['class'] += ' ' + jquery_input_class
				else:
					field.widget.attrs.update({'class':jquery_input_class})

			if field.widget.__class__ == forms.widgets.Select:
				if field.widget.attrs.has_key('class'):
					field.widget.attrs['class'] += ' ' + jquery_combo_class
				else:
					field.widget.attrs.update({'class':jquery_combo_class})

	class Meta:
		model = Trip
		widgets = {
			'place_from': forms.Select(),
            'place_to': forms.Select(),
            'type': forms.Select(),
            'name': forms.TextInput(),
            'comments': Textarea(attrs={'cols': 40, 'rows': 5}),
			'phone_number':forms.TextInput(),
        }		
		
	def clean(self):
		print '--------------------------------> call clean'
		
		cleaned_data = super(TripForm, self).clean()
		date = cleaned_data.get("date")
		
		if date is None:
			self._errors["date"] = ErrorList([DEFAULT_VALIDATION['empty_date']]) 
			
		else:

			# now = datetime.datetime.utcnow().replace(tzinfo=utc) + datetime.timedelta(hours = 1)
			now = datetime.datetime.utcnow().replace(tzinfo=utc) # + datetime.timedelta(hours = 1)
			print 1111111111111
			print now
			now = timezone.make_naive(now, timezone.get_default_timezone())
			print 2222222222222
			print now
			print date
			# now = timezone.localtime(timezone.now()) - datetime.timedelta(hours = 1)
			if date < now:
				self._errors["date"] = ErrorList([DEFAULT_VALIDATION['less_current_date']]) 		

		place_from = cleaned_data.get("place_from")
		if place_from is None:
			self._errors["place_from"] = ErrorList([DEFAULT_VALIDATION['empty_place_from']])
	
		place_to = cleaned_data.get("place_to")
		if place_to is None:
			self._errors["place_to"] = ErrorList([DEFAULT_VALIDATION['empty_place_to']])
	
		type = cleaned_data.get("type")
		if type is None:
			self._errors["type"] = ErrorList([DEFAULT_VALIDATION['empty_type']])

		name = cleaned_data.get("name")
		if name is None:
			self._errors["name"] = ErrorList([DEFAULT_VALIDATION['empty_name']])
				
#TODO		
		phone_number = cleaned_data.get("phone_number")
		if phone_number != None and len(phone_number) < 11:
			self._errors["phone_number"] = ErrorList([DEFAULT_VALIDATION['invalid_phonenumber_length']])
		
		return cleaned_data

class TripFormCaptcha(TripForm): #DivModelForm
	captcha = ReCaptchaField()
