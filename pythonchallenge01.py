#-*-coding:utf-8-*-
import string

content = """g fmnc wms bgblr rpylqjyrc gr zw fylb.
           rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q
           ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

charc = string.lowercase
url = 'map'
a = string.maketrans(charc, charc[2:]+charc[0:2])

s1 = content.translate(a)
s = url.translate(a)

print s1

print "http://www.pythonchallenge.com/pc/def/{map}.html".format(map=s)