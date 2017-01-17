#!/usr/bin/python

import sqlite3

conn=sqlite3.connect("example.db")
c=conn.cursor()

#create table
c.execute('''create table stocks
        (data text, trans text, symbol text, qty real, price real)''')
#insert a row of data
c.execute("insert into stocks values('2006-01-05','buy','rhat',100,35.14)")

purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

#save the changes
conn.commit()

c.execute("select * from stocks")
#print c.fetchone()
for row in c.execute('SELECT * FROM stocks ORDER BY price'):
    print row

#close
conn.close()


