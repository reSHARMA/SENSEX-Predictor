#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
from pprint import pprint
import string
import time
def sensex():
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
    b = a.select(".BdT")
    c = b[0]
    d = b[1]
    s1 = c.text
    s2 = d.text
    return [s1[0:11] , s1[11:13] + s1[14:20] , s2[0:11] , s2[11:13] + s2[14:20]]
