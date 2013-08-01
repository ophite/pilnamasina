import os
import sys
import os.path
sys.path.append('/var/www/domniak/data/www/pilnamasina.lt')
sys.path.append('/var/www/domniak/data/www/pilnamasina.lt/helloworld')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
