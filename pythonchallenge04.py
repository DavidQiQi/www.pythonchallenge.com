#-*-coding:utf-8-*-

from bs4 import BeautifulSoup as bs
import requests
import re


url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'

def gethtml(url):
    r = requests.get(url)
    if r.text[-1].isdigit():
        s = re.compile('.*?(\d+)$')
        id = re.findall(s, str(r.text))[0]
        return id
    else:
        return r.text

r = requests.get(url)
if  r.encoding != 'UTF-8':
    r.encoding == "GBK"
soup = bs(r.text, 'html.parser')
newurl = url + "?" +soup.select('center > a')[0]['href'].split('?')[1]

newurll = newurl.split('=')[0] + '='
id = gethtml(newurl)
reg = re.compile('\.html$')
for i in xrange(400):
    if re.findall(reg, id):
        print id
        break
    urll = newurll + id
    if id == '16044':
        id = str(int(id) / 2)
        continue
    else:
        id = gethtml(urll)
    #print urll
    #print id













