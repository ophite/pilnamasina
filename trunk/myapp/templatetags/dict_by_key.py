# coding=utf-8 
#import re
from django import template
register = template.Library()

@register.filter
def dict_getbykey(the_dict, key):
	print '1111111111111111111111122222222222222222222222222333333333333333 call'
	print 'the_dict', the_dict
	print 'key', key
	
	if the_dict is None or the_dict == '':
		return key
			
	object = the_dict.get(key, None)
	
	if object is None:
		return key
		
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
			#print 1111111111111111111111122222222222222222222222222333333333333333
			#print ','.join(unicode(obj) for obj in object[:l])
			return ','.join(unicode(obj) for obj in object[:l])

	return object