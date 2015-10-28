#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      gang
#
# Created:     01/10/2014
# Copyright:   (c) gang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
#coding=utf-8

import urllib2, cookielib, urllib, sys
from bs4 import BeautifulSoup

def getUniversityName():
    #BeautifulSoup(markup, "lxml")
    cj=cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)

    mldm = '08'
    mlmc = 'นคัง'
    output = open(mldm+'xiaoming.txt','w')

    postdata = urllib.urlencode({'mldm':mldm,'mlmc':mlmc})
    req=urllib2.Request(url='http://yz.chsi.com.cn/zsml/queryAction.do',data=postdata)
    response = urllib2.urlopen(req).read().decode('utf8')
    soup = BeautifulSoup(response,fromEncoding='utf8')
    page_str = soup.find(id='page_total').get_text()[2:]
    page_num = int(page_str)
    #login

    for i in range(1,page_num+1):
        postdata = urllib.urlencode({'mldm':mldm,'mlmc':mlmc,'pageno':i})
        req=urllib2.Request(url='http://yz.chsi.com.cn/zsml/queryAction.do',data=postdata)
        response = urllib2.urlopen(req).read().decode('utf8')
        soup = BeautifulSoup(response,fromEncoding='utf8')
        confirme = str(soup.find(id='sch_list').find_all("td")).strip().decode('utf8')
        start = soup.find(id='sch_list')

        while(start.find_next('td')):
            uniName = start.find_next('td').get_text()[7:]
            start = start.find_next('td')
            start = start.find_next('td')
            start = start.find_next('td')
            start = start.find_next('td')
            start = start.find_next('td')
            start = start.find_next('td')
            print>>output,uniName
#    for university in soup.find(id='sch_list').find_all('a'):
#        print str(university).strip().decode('utf8')
    output.close()

getUniversityName()
#if __name__ == '__main__':
#   partsUpload(sys.argv)
