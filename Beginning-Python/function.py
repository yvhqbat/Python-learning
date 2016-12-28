#!/usr/bin/python

def hello(name):
    return "hello "+name+"!"

print hello("liudong")

def fibs(num):
    "this is a function calculate fibs"
    result=[0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result

print fibs(8)
print fibs.__doc__

x=10

def not_chage_global():
    x=13
print x

def change_global():
    global x
    x=x+1
change_global()
print x

#di gui
def factorial(n):
    result=n
    for i in range(1,n):
        result*=i
    return result
def factorial_re(n):
    if n==1:
        return 1
    else:
        return n*factorial_re(n-1)

print factorial(3)
print factorial(3)

