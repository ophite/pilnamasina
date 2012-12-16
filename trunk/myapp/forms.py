from django import forms
from django.core import validators
from django.forms import ModelForm, Textarea
from django.forms.util import ErrorList
from django.utils.timezone import utc

import datetime

from myapp.models import Trip

from recaptchawidget.fields import ReCaptchaField 
	
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

class TripForm(DivModelForm):
	#date = forms.DateTimeField(label='Date C', widget=forms.DateTimeField(attrs={'class':'form-field'}))
	captcha = ReCaptchaField()
	
	class Meta:
		model = Trip
		widgets = {
            'place_from': forms.Select(),
            'place_to': forms.Select(),
            'name': forms.TextInput(),
            'comments': Textarea(attrs={'cols': 40, 'rows': 5}),
			'phone_number':forms.TextInput(),
            'date': forms.TextInput(attrs={'class':'ui-combobox-input ui-state-default ui-widget ui-widget-content ui-corner-left ui-corner-right'}),
        }
		
	def clean(self):
		cleaned_data = super(TripForm, self).clean()
		#self.error_class([u'You must input date to create new trip'])		
		date = cleaned_data.get("date")

		if date is None:
			self._errors["date"] = ErrorList([u'You cannot input empty date']) 
		else:
			now = datetime.datetime.utcnow().replace(tzinfo=utc)
			if date < now:
				self._errors["date"] = ErrorList([u'You cannot input less then current date']) 		

		place_from = cleaned_data.get("place_from")
		if place_from is None:
			self._errors["place_from"] = ErrorList([u'You must input place from to create new trip'])
	
		place_to = cleaned_data.get("place_to")
		if place_to is None:
			self._errors["place_to"] = ErrorList([u'You must input place to to create new trip'])

		name = cleaned_data.get("name")
		if name is None:
			self._errors["name"] = ErrorList([u'You must input name to create new trip'])
		
		return cleaned_data