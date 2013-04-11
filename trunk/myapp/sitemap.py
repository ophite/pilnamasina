from django.core.urlresolvers import reverse
from django.contrib.sitemaps import Sitemap
import datetime

#class S	itemap(Sitemap):
 #   def __init__(self, names):
  #      self.names = names
#
 #   def items(self):
  #      return self.names
#
 #   def changefreq(self, obj):
  #      return 'monthly	'
#
 #   def lastmod(self, obj):
  #      return datetime.datetime.now()
#
 #   def location(self, obj):
  #      return reverse(obj)

  
class AbstractSitemapClass():
#	changefreq = 'monthly'
	url = None
	def get_absolute_url(self):
		return self.url
		
class StaticSitemap(Sitemap):
	pages = {
             'home':'/', 	#Add more static pages here like this 'example':'url_of_example',
             'add':'/add/',
			}
	main_sitemaps = []

	for page in pages.keys():
		sitemap_class = AbstractSitemapClass()
		sitemap_class.url = pages[page]
		main_sitemaps.append(sitemap_class)
		
	def items(self):
		return self.main_sitemaps   
		
	lastmod = datetime.datetime(2013, 4, 11)   #Enter the year,month, date you want in yout static page sitemap.
	priority = 1
	changefreq = "monthly" 
