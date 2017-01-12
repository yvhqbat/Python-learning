#!/usr/bin/python

import MySQLdb as mdb

#connect to the database
conn = mdb.connect('localhost', 'root', 'liudongwho')

cursor = conn.cursor()
cursor.execute('SHOW DATABASES')
results = cursor.fetchall()
for result in results:
    print result

DB_NAME='ld'
conn.select_db(DB_NAME)
cursor.execute('select * from students')
results=cursor.fetchall()
for result in results:
    print result


