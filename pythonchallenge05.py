#-*-coding:utf-8-*-
# Author: david.qi 
# mail: davis.ying@gmail.com

### peak hell sound pickle

import requests
from bs4 import BeautifulSoup as bs
import pickle
import os


def abc((a, b)):
    return a * b

url = 'http://www.pythonchallenge.com/pc/def/peak.html'
r = requests.get(url)

soup = bs(r.text, 'html.parser')
fileurl = soup.select('peakhell')[0]['src']

bannerurl = url.replace('peak.html', fileurl)

pr = requests.get(bannerurl)
if pr.ok:
    content = pickle.loads(pr.content)
    print content

for i in content:
    # print i
    print ''.join(map(abc, i))





