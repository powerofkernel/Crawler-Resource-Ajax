
import re
from lib.http import http_craw
from termcolor import colored

def search_tag_script(html):
	scripts_arr = []
	#print text
	script_match = re.findall(ur'<script(.+?)></script>', html)

	if len(script_match) != 0:
		for script in script_match:
			#print script,""
			script_src_match = re.findall(ur'src=\"(.+?)\"', script)
			for source_script in script_src_match:
				#print "http://"+url+source_script,""
				scripts_arr.append(source_script)
		return scripts_arr
	else:
		return False

def find_functions(scr):
	if http_craw.check_http(scr) == False:	# si no existe file path , se devuelve hacia atras ../
		scr = scheme + "://" + netloc + path + "../" + tags_index

	print colored("\n[+] Script\t: ", 'blue'), colored(scr , 'white', attrs=['reverse', 'blink']),
	text_script = http_craw.http_get(scr)
	text_split  = re.compile("\n").split(text_script)
	cuenta_linea= 0;
			
	estado_function = False
	estado_ajax		= False

	for text_linea in text_split: ## recorre linea a linea por archivo js
		cuenta_linea = cuenta_linea+1
		#print text_linea
		ajax_match = re.search(ur'function(.*)', text_linea) # arr con matchs de funciones
		#print ajax_match

		if ajax_match is not None:
			estado_function = True
			print colored("\n[+] Linea " + str(cuenta_linea) + "\t: ", 'blue') , colored( text_linea , 'red')
			ajax_match = re.sub('{|}', '', ajax_match.group()) # remueve corchetes
			#print "\t" + ajax_match
		#print ajax_match.group()
		if estado_function == True:
			ajax_match = re.search(ur'(.*)ajax(.*)', text_linea) # arr con matchs de funciones
			if ajax_match is not None:
				estado_ajax = True
				print colored("\t\t" + ajax_match.group() + "\n", "yellow"),
				#print ajax_match.group()

		if estado_function == True and estado_ajax == True:
			#print text_linea,""
			ajax_match = re.search(ur'url(.*)|data(.*)', text_linea) # arr con matchs de funciones
			if ajax_match is not None:
				print colored("\t\t\t" + ajax_match.group() + "\n", "yellow"),