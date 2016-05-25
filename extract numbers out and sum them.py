# Note - this code must run in Python 2.x 

f = open('Regex_sum_267874.txt','r')
cnts = f.read()
import re
y = [int(s) for s in re.findall(r'\d+',cnts)]
sum(y)
y = [int(s) for s in re.findall('[0-9]+',cnts)]
sum(y)