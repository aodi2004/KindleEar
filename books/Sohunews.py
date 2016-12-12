#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag
import os

    
def getBook():
    return Sohunews


class Sohunews(BaseFeedBook):
    title               = u'搜狐新闻'
    description         = u'新闻天天看'
    __author__          = 'aodi2004'
    language            = 'zh-cn'
    feed_encoding       = "gbk"
    page_encoding       = "gbk"
    mastheadfile        = "mh_nfzm.gif"
    coverfile           = "cv_nfzm.jpg"
    #deliver_days        = []
    #deliver_times       =[6,12,17]
    keep_image = False    
    #needs_subscription  = True

    def ParseFeedUrls(self):
        #login_url = "http://passport.infzm.com/passport/login"

        content_url = "http://m.sohu.com/"
        opener = URLOpener(self.host, timeout=60)
        result = opener.open(content_url)

        content = result.content.decode('utf-8')
        debug_mail(content,'msohu.html')

        

        
        content_url = "http://www.sohu.com/"
        urls = []
        opener = URLOpener(self.host, timeout=60)
        #login_form = {"loginname":self.account, "password":self.password}
        #login_response = opener.open(login_url, data=login_form)
        #opener.SaveCookies(login_response.header_msg.getheaders('Set-Cookie'))
        result = opener.open(content_url)

        content = result.content.decode(self.feed_encoding)
        soup = BeautifulSoup(content, "lxml")
        sec_titles = []
        
                    
        for top_news in soup.find_all('div', {'id': 'top_news'}):
            for desc_news in top_news.find_all('a'):
                url = desc_news['href']
                feed_content = opener.open(url).content.decode(self.feed_encoding)
                feed_soup = BeautifulSoup(feed_content, "lxml")

                if feed_soup.find(id='contentText'):
                    urls.append((self.title, desc_news.text, url, feed_soup.find(id='contentText')))       
        return urls
    
