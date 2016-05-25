# Extract data from xml
# Note - this code must run in Python 2.x and you must download
# Sample data: http://python-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://python-data.dr-chuck.net/comments_267876.xml (Sum ends with 1)

import xml.etree.ElementTree as ET
import urllib2

address = raw_input('Enter location: ')
if len(address) < 1 : url = 'http://python-data.dr-chuck.net/comments_267876.xml'

print 'Retrieving', url
uh = urllib2.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)
com = tree.findall('comments/comment')
print 'Count: ', len(com)
counts = []
for item in com:
    co = item.find('count').text
    counts.append(int(co))
print 'Sum: ', sum(counts)