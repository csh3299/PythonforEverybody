# Using the GeoJSON API
# Python 2.7
# API End Points
# To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:
# http://python-data.dr-chuck.net/geojson

import urllib
import json

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break
	
    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        continue

#    print json.dumps(js, indent=4)
    place_id = js["results"][0]["place_id"]
    print 'Place id', place_id
#    location = js['results'][0]['formatted_address']
#    print location

