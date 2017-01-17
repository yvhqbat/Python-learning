#!/usr/bin/python

class Person:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def greet(self):
        print "hello world! i'm %s." % self.name

    #private
    def setAge(self,age):
        self.__age=age
    def getAge(self):
        return self.__age

foo=Person()
bar=Person()
foo.setName("liudong")
bar.setName("caipei")
foo.greet()
bar.greet()
print foo.name
print bar.name

foo.setAge(24)
bar.setAge(25)
print foo.getAge()
print bar.getAge()
#print foo.__age
#print bar.__age

class People(Person):
    def method(self):
        print "i have a self"
    def __function(self):
        print "i do not have ..."
    def call_function(self):
        print "i call private function"
        self.__function()

people1=People()
people1.setName("people")
people1.setAge(23)
print people1.getName()
print people1.getAge()
people1.method()
#people1.function()
people1.call_function()

print issubclass(People,Person)
print isinstance(foo,Person)
print isinstance(people1,People)
print isinstance(people1,Person)
print hasattr(Person,'setName')
print " has setname"
