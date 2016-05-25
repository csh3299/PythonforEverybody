# Scraping HTML Data with BeautifulSoup
# Note - this code must run in Python 2.x 
# Sample data: http://python-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://python-data.dr-chuck.net/comments_267879.html (Sum ends with 16)



from bs4 import BeautifulSoup
import urllib2

url = raw_input('Enter - ')
if len(url) < 1 : url = "http://python-data.dr-chuck.net/comments_267879.html"
html = urllib2.urlopen(url)

soup = BeautifulSoup(html)
spans = soup.find_all('span')

# Retrieve all numbers of the span tags
import re
spans = str(spans)
ys = re.findall('>([0-9]+)<',spans)
y = [int(s) for s in ys]
print sum(y)


