#!/usr/bin/python

d=dict(name="liudong",age=24);
print d
d["love"]="caipei"

print d["name"]
print d["age"]
print d["love"]
print len(d)

print(d.get("xixi"))
print d.has_key("name")
print d.has_key("xiix")

d.pop("love")
print d.items()

## update
d={
  "title":"python web site",
  'url':'http://www.python.org',
  'changed':'mar 14 2008'
  }
print d
x={'title':'python language website'}
d.update(x)
print d
