#!/usr/bin/python

import requests
import json
import urllib
import lxml.html
import re
count = 1
dwnldr = "uploaded"
testwoed = "Paul"
my_list = list()
my_list2 = list()
while (count < 11):
    print 'This is page:', count

    connection = urllib.urlopen('http://rlsbb.com/page/%d' % count)

    dom = lxml.html.fromstring(connection.read())

    for link in dom.xpath('//a/@href'):
      my_list.append(link)
      my_list2.append([s for s in my_list if dwnldr in s])


    count = count + 1

print s for s in my_list if dwnldr in s

def send_to_pyload(link):
    payload = {'username': 'admin', 'password': 'openmediavault'}
    with requests.session() as s:
        s.post('http://192.168.0.29:8888/api/login', data=payload)
    payload = {'name': 'series', 'links': [link]}
    payloadJSON = {k: json.dumps(v) for k, v in payload.items()}
    r = s.post('http://192.168.0.29:8888/api/adddPackage', data=payloadJSON)
    print r.text
    return
