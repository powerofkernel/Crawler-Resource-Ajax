import urllib2
import re

def http_get(url) :
	req = urllib2.Request(url)
	#req.addheaders.append(('Cookie', 'ci_session=bop3643ooqdcd7dlbhmqv7sdsahgug8v'))
	req.add_header('Cookie', 'ci_session=bop3643ooqdcd7dlbhmqv7sdsahgug8v')
	req.add_header('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13) AppleWebKit/603.1.13 (KHTML, like Gecko) Version/10.1 Safari/603.1.13')
	res = urllib2.urlopen(req)
	html = res.read()
	return html

def check_http(target) :
	try:

	    response = urllib2.urlopen(target) 
	    return response.getcode()
	except IOError, e:
		return False
	'''
	    if hasattr(e, 'code'): # HTTPError
	        #print e.code
	        return False
	    elif hasattr(e, 'reason'): # URLError
	        #print "# Imposible conectar"
	        return False
	    else:
	        #raise
	        return False
	#return False
	'''
