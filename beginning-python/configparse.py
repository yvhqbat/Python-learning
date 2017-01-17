#!/usr/bin/python

from ConfigParser import ConfigParser

CONFIGFILE="config.txt"
config=ConfigParser()
config.read(CONFIGFILE)

print config.get('messages','question')


