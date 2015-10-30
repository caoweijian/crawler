#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      caoweijian
#
# Created:     27/10/2015
# Copyright:   (c) caoweijian 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#coding=utf-8

import urllib2, cookielib, urllib, sys
from bs4 import BeautifulSoup

def getInformation(mldm):
    mlmc=''
    cj=cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)

    output = open(mldm+'result.txt','w')

    postdata = urllib.urlencode({'mldm':mldm,'mlmc':mlmc})
    req=urllib2.Request(url='http://yz.chsi.com.cn/zsml/queryAction.do',data=postdata)
    response = urllib2.urlopen(req).read().decode('utf8')
    soup = BeautifulSoup(response)
    page_str = soup.find(id='page_total').get_text()[2:]
    page_num = int(page_str)
    #print page_num

    for i in range(1,page_num+1):
        postdata = urllib.urlencode({'mldm':mldm,'mlmc':mlmc,'pageno':i})
        req=urllib2.Request(url='http://yz.chsi.com.cn/zsml/queryAction.do',data=postdata)
        response = urllib2.urlopen(req).read().decode('utf8')
        soup = BeautifulSoup(response)
        start = soup.find(id='sch_list')
        #get University Name
        while(start.find_next('td')):
            uniName = start.find_next('td').get_text()[7:]
            #print uniName
            start = start.find_next('td')
            start = start.find_next('td')
            start = start.find_next('td')
            start = start.find_next('td')
            start = start.find_next('td')
            start = start.find_next('td')
            readurl = 'http://yz.chsi.com.cn/zsml/querySchAction.do?ssdm=&dwmc='+str(uniName).encode('utf8')+'&mldm='+mldm+'&mlmc='+mlmc+'&yjxkdm=&zymc='
            #print readurl
            searchResult = urllib2.urlopen(readurl).read()
            resultSoup = BeautifulSoup(searchResult)
            result_page_str = resultSoup.find(id='page_total').get_text()[2:]
            result_page_num = int(result_page_str)
            #print result_page_num
            for j in range(1,result_page_num+1):
                readurl = 'http://yz.chsi.com.cn/zsml/querySchAction.do?ssdm=&dwmc='+str(uniName).encode('utf8')+'&mldm='+mldm+'&mlmc='+mlmc+'&yjxkdm=&zymc=&pageno='+str(j)
                searchResult = urllib2.urlopen(readurl).read()
                resultSoup = BeautifulSoup(searchResult)
                #print str(resultSoup).decode('utf8')
                subject = resultSoup.find(id='sch_list')

                while(subject.find_next('td')):
                    str1 = subject.find_next('td').get_text()
                    subject = subject.find_next('td')
                    str2 = subject.find_next('td').get_text()
                    subject = subject.find_next('td')
                    str3 = subject.find_next('td').get_text()
                    subject = subject.find_next('td')
                    subject = subject.find_next('td')
                    subject = subject.find_next('td')
                    subject = subject.find_next('td')
                    subject = subject.find_next('td')
                    subject = subject.find_next('td')
                    try:
                        print>>output,"%s\t%s\t%s\t%s\t%s\t%s\t%s" %(uniName,str1[1:4],str1[5:],str2[1:7],str2[8:],str3[1:3],str3[4:])
                    except:
                        print>>output,"%s\t%s\t%s\t%s\t%s\t%s\t%s" %(uniName,str1[1:4],str1[5:],str2[1:7],str2[8:],str3[1:3],str3[4:-1])
    output.close()

mldm = ['01','02','03','04','05','06','07','08','09','10','11','12','13']
for i in range(len(mldm)):
    getInformation(mldm[i])