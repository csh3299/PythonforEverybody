#Extract data from JSON
# Python 2.7
# Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://python-data.dr-chuck.net/comments_267880.json (Sum ends with 96)
import json
import urllib2

address = raw_input('Enter location: ')
if len(address) < 1 : url = 'http://python-data.dr-chuck.net/comments_267880.json'

print 'Retrieving', url
uh = urllib2.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
info = json.loads(data)
print 'Count: ', len(info)
counts = []
for item in info['comments']:
    co = item['count']
    counts.append(int(co))
print 'Sum: ', sum(counts)
