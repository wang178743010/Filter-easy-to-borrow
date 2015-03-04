#coding:utf-8
import requests
from BeautifulSoup import BeautifulSoup
r = "http://www.huyibank.com/"
resp = requests.get(r)
bs = BeautifulSoup(resp.content)

span = bs.findAll("span",{"class":"w1"}) 
for i in span:
      for x in i.findAll("div"):
            print x.text
span1 = bs.findAll("span",{"class":"w3"})
for i in span1:
      print i.text
span2 = bs.findAll("span",{"class":"w5"})
for i in span2:
      print i.text
span3 = bs.findAll("span",{"class":"w7"})
for i in span3:
      print i.text
url = span + span1 + span2 + span3
for i in url:
      print i.text
