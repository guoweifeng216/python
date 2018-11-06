import urllib2

reponse = urllib2.urlopen("http://baidu.com")
print reponse.read()