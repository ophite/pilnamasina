# coding=utf-8 
#import re
from django import template
register = template.Library()

@register.filter
def dict_getbykey(the_dict, key):
		
	object = the_dict[key]
	if isinstance(object, (list)):
		l=len(object)
		#object
		if l==1:
			return "\\'%s\\'" % object[0]
		#list 
		else:   
			#j = re.compile('[[" \]]')
			#str = ','.join("\\'" + unicode(obj) + "\\'" for obj in object[:l])
			#x =  "%s" % str
			#r = j.sub('',x).split(',')
			return ','.join(unicode(obj) for obj in object[:l])

	return object