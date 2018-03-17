#!/usr/bin/python

import platform
import os
import urllib2
import re

from lib.http import http_craw
from lib.craw import ajax_craw
from lib.misc import misc

from termcolor import colored
from urlparse import urlparse

if platform.system() == "Windows":
	os.system('cls')
else:
	os.system('clear')
misc.logo()

url = "http://localhost/"

### MAIN
urlstrip= urlparse(url)
scheme  = urlstrip.scheme
netloc	= urlstrip.netloc
path 	= urlstrip.path

if http_craw.check_http(url) == 200:
	scr  = ""
	text = http_craw.http_get(url) # get text html principal index
	#print text
	tag_match = re.findall(ur'<(.+?)>', text)
	for tags_all in tag_match:
		#print tags_all +"\n",
		match_event = re.compile('(.*?)onclick(.*?)|(.*?)onkey(.*?)', re.IGNORECASE)
		#print tags_all,
		#print re.match(u'(.*?)onclick(.*?)', tags_all)
		if match_event.match(tags_all) is not None:
			print tags_all + "\n",
	'''
	tags 	= ajax_craw.search_tag_script(text) # busca tags scripts

	for tags_index in tags:	# recorre tags scripts
		scr = scheme + "://" + netloc + path + tags_index # arma url
		## checkar profundidad de path con respuesta http
		ban_match = re.search(ur'jquery|bootstrap', tags_index) # salta lib script jquery
		if ban_match == None:
			ajax_craw.find_functions(scr)
	'''			


else:
	url = "https://" + netloc + path
	print "# https check "+ url
	