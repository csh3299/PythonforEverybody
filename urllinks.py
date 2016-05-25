# Following Links in HTML Using BeautifulSoup
# Note - this code must run in Python 2.x 
# Sample problem: Start at http://python-data.dr-chuck.net/known_by_Fikret.html 
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
# Last name in sequence: Anayah
# Actual problem: Start at: http://python-data.dr-chuck.net/known_by_Kaye.html 
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: M


from bs4 import BeautifulSoup
import urllib2

url = raw_input('Enter url- ')
if len(url) < 1 : url = "http://python-data.dr-chuck.net/known_by_Kaye.html"

count = raw_input('Enter count- ')
if len(count) < 1 : count = 7
pos = raw_input('Enter position- ')
if len(pos) < 1 : pos = 18

names = []
while count > 0:
    print "Retrieving: {0}".format(url)
    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html)
    tags = soup.find_all('a')
    url = tags[pos-1].get('href')
    name = str(url)
    names.append(name)
    count -= 1
print "Retrieving: ", names[-1]