#-*-coding:utf-8-*-

import urllib2
import re
import pickle
import string
import os


def download(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html = response.read()
    return html

def save(html,filename):
    f = open(filename,'w')
    pickle.dump(html, f)
    f.close()
    #print 'save {} success'.format(filename)


def see(filename):
    f = open(filename,'r',buffering=500)
    content = pickle.load(f)
    f.close()
    return content

uri = 'http://www.pythonchallenge.com/pc/def/'
url = 'http://www.pythonchallenge.com/pc/def/equality.html'
filena = url.split('/')[-1]
filename = os.path.join("C:\me\pycharm\python",filena)

s = download(url)
save(s,filename)
content = see(filename)

s = re.compile('<!--[^>]*-->')

s1 = re.compile('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]')

m = re.findall(s, content)


m1 = re.findall(s1, str(m))  #m1 = re.findall(s1, m[0])

print  "link url:" + uri + ''.join(map(lambda x:x[4], m1)) + '.html'



