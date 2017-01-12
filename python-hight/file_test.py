#!/usr/bin/python

f=open('somefile.txt','w')
f.write('hello')
f.write(' world!')
f.close()

f=open('somefile.txt','r')
text=f.read()
print text
f.close()
