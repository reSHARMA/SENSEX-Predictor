#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
from pprint import pprint
import string
import time
def gold():
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
    b = a.select(".prc")
    c = (b[0].text).replace(",","");
    d = a.select(".nte-day-yest")
    e = d[0].select("b")
    f = (((e[0].text).split(" "))[0]).replace(",","")
    print(c + " " + f)
    return [c,f]
gold()
