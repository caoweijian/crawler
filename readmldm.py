#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      cwj
#
# Created:     27/10/2015
# Copyright:   (c) cwj 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import urllib2, cookielib, urllib, sys
from bs4 import BeautifulSoup

def readmldm():
    #BeautifulSoup(markup, "lxml")
    cj=cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)

    mldm = '08'
    mlmc = 'นคัง'
    input = open(mldm+'uni.txt')
    output = open(mldm+'result.txt','w')

    for i in input:
        i = i.strip('\n')
        readurl = 'http://yz.chsi.com.cn/zsml/querySchAction.do?ssdm=&dwmc='+i+'&mldm='+mldm+'&mlmc='+mlmc+'&yjxkdm=&zymc='
        #print readurl

        response = urllib2.urlopen(readurl).read()
        soup = BeautifulSoup(response)

        page_str = soup.find(id='page_total').get_text()[2:]
        page_num = int(page_str)
        #print page_num
        for j in range(1,page_num+1):
            readurl = 'http://yz.chsi.com.cn/zsml/querySchAction.do?ssdm=&dwmc='+i+'&mldm='+mldm+'&mlmc='+mlmc+'&yjxkdm=&zymc=&pageno='+str(j)
            response = urllib2.urlopen(readurl).read()
            soup = BeautifulSoup(response)
            #print str(soup).decode('utf8')
            start = soup.find(id='sch_list')
            #print str(start).decode('utf8')

            while(start.find_next('td')):
                str1 = start.find_next('td').get_text()
                start = start.find_next('td')
                str2 = start.find_next('td').get_text()
                start = start.find_next('td')
                str3 = start.find_next('td').get_text()
                start = start.find_next('td')
                start = start.find_next('td')
                start = start.find_next('td')
                start = start.find_next('td')
                start = start.find_next('td')
                start = start.find_next('td')
                try:
                    #output.write("%s %s %s %s %s %s %s\n" %(i.decode('utf8'),str1[1:4],str1[5:],str2[1:7],str2[8:],str3[1:3],str3[4:]))
                    print>>output,"%s %s %s %s %s %s %s" %(i.decode('utf8'),str1[1:4],str1[5:],str2[1:7],str2[8:],str3[1:3],str3[4:])
                except:
                    print>>output,"%s %s %s %s %s %s %s" %(i.decode('utf8'),str1[1:4],str1[5:],str2[1:7],str2[8:],str3[1:3],str3[4:-1])
    output.close()

#if __name__ == '__main__':
readmldm()