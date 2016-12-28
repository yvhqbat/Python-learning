#!/usr/bin/python

from urllib import urlopen
#import re
#p=re.compile('<h3><a .*?><a .*? href=(.*?)">(.*?)</a>')
text=urlopen('http://www.baidu.com')
#for url,name in p.findall(text):
#    print '%s (%s)'%(name,url)
print text.read()

