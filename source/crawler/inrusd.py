#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
from pprint import pprint
import string
import time
def inrusd():
    headers = {}
    headers['Accept'] = \
        'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    headers['Accept-Encoding'] = 'gzip, defalte'
    headers['Connection'] = 'keep-alive'
    headers['User-Agent'] = \
        'Mozilla/5.0 (X11; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0'
    with urllib.request.urlopen("tradesecret") as conn:
        rr=conn.read()
    a = BeautifulSoup(rr,'html.parser')
    b = a.select("tbody")
    c = b[0]
    d = c.children
    next(d)
    e = next(d)
    f = next(d)
    g = (((e.select("td"))[2].text).split(" "))[0]
    h = (((f.select("td"))[2].text).split(" "))[0]
    pprint(g + "  "  + h)
    return [g,h]
inrusd()
