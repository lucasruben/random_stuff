import json
import urllib2

data = {'first_name':   'Lucas',
    'last_name': 'Ruben',
    'email':  'lukasrub@gmail.com',
    'phone': '+5493425947430',
    'cover_letter': 'Ruben',
    'urls': [	'http://www.westernoriental.com', 
    			'http://www.rainbowtours.co.uk',
    			'http://www.regent-holidays.co.uk'
    		]}
data_json = json.dumps(data)
url = 'https://app.close.io/hackwithus/'
r = urllib2.Request(url)
r.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(r, data_json)
print response.getcode()
print response.read()
response.close()
