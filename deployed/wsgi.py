import os
import sys

sys.path.append('/var/www/domniak/data/www/application')
sys.path.append('/var/www/domniak/data/www/pilnamasina.lt/helloworld')

#os.environ['PYTHON_EGG_CACHE'] = '/var/www/domniak/data/www/.python-egg'
os.environ['DJANGO_SETTINGS_MODULE'] = 'helloworld.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
