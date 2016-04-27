#-*-coding:utf-8-*-

import urllib2
import re
import pickle
import string



def download(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html = response.read()
    return html

def save(html,file="C:\me\pycharm\python\\file"):
    f = open(file,'w')
    pickle.dump(html, f)
    f.close()

def see(filename="C:\me\pycharm\python\\file"):
    f = file(filename)
    content = pickle.load(f)
    f.close()
    return content

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'

s = download(url)
save(s)
content = see()

s = re.compile('<!--[^>]*-->')


conte =  re.findall(s, content)

s1 = re.compile('[a-z]',re.I)

charat = re.findall(s1, conte[1])

#print conte[0]
print  "http://www.pythonchallenge.com/pc/def/{}.html".format(''.join(charat))


