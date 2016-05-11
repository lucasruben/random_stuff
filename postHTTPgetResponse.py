import json
import urllib2
#JSON with the data we want to send
data = {
    'first_name':   "name",
    'last_name': "lastName",
    'email':  "email",
    'phone': "999999999",
    'cover_letter': "letter",
    'urls': [	"URL1", 
    			"URL2",
    			"URL3"
    		]}
data_json = json.dumps(data)
url = 'targetURL'
r = urllib2.Request(url)
r.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(r, data_json)
print response.getcode()
print response.read()
response.close()
