#!/usr/bin/python
import re
import urllib

link = "http://rlsbb.com/page/2/"
f = urllib.urlopen(link)
myfile = f.read()

urls = re.findall('http[s]?://www.uploadable.ch(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', myfile)

print urls

payload={'username':'admin','password':'openmediavault'}
    s.post('http://192.168.0.29:9666/api/login', data=payload)
    payload={'name':'series','links':['http://depositfiles.com/files/6u8gr6yx5']}
    
   rs = requests.post('http://192.168.0.29:9666/api/addPackage', data=payloadJSON)
