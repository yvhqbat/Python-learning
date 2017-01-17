#!/usr/bin/python

#this is a comment
#chmod a+x array.py

edward=['Edward Gumby',42]
print edward
print edward[0]
print edward[1]

numbers=[1,2,3,4,5,6,7,8,9]
print numbers[3:5]
#[4,5]
print numbers[0:10:2]
#[1,3,5,7,9]

#merge numbers and numbers2
numbers2=[12,13,14]
print numbers+numbers2
#[1,2,3,4,5,6,7,8,9,12,13,14]

print [3]*5
#[3, 3, 3, 3, 3]

#an example
sentence=raw_input('sentence: ')
screen_width=80
text_width=len(sentence)
box_width=text_width+6
left_margin=(screen_width-box_width)//2
print
print ' '*left_margin + '-'*box_width
print ' '*left_margin + '|' + ' '*(box_width-2) + '|'
print ' '*left_margin + '|  ' + sentence + '  |'
print ' '*left_margin + '|' + ' '*(box_width-2) + '|'
print ' '*left_margin + '-'*box_width
#sentence: i love you
#
#                                ----------------
#                                |              |
#                                |  i love you  |
#                                |              |
#                                ----------------


# 'in' operator
database=[ 
  ['albert','1234'],
  ['dilbert','4242'],
  ['liudong','liudongwho'],
  ['smith','4532'] 
]
username=raw_input('username=')
password=raw_input('password=')
if [username,password] in database : 
  print "access granted"
else:
  print "access denied"


# list


# tuple


# dict

