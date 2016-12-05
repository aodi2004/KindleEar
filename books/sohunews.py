#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag
import os

    
def getBook():
    return sohunews


class sohunews(BaseFeedBook):
    title               = u'搜狐新闻new and it'
    description         = u'新闻天天看'
    __author__          = 'aodi2004'
    language            = 'zh-cn'
    feed_encoding       = "utf-8"
    page_encoding       = "utf-8"
    mastheadfile        = "mh_nfzm.gif"
    coverfile           = "cv_nfzm.jpg"
    #deliver_days        = []
    #deliver_times       =[6,14,17]
        
    #needs_subscription  = True

    def ParseFeedUrls(self):
        #login_url = "http://passport.infzm.com/passport/login"
        content_url = "http://m.sohu.com/"
        urls = []
        opener = URLOpener(self.host, timeout=60)
        result = opener.open(content_url)

        content = result.content.decode(self.feed_encoding)
        soup = BeautifulSoup(content, "lxml")
        ii=0        
                    
        for top_news in soup.find_all('section', {'class': 'ls'}):
            ii+=1
            if ii==2:
                for news in top_news.find_all('a'):
                    url = news['href']
                    feed_content = opener.open(url).content.decode(self.feed_encoding)
                    feed_soup = BeautifulSoup(feed_content, "lxml")
                    if feed_soup.find('article'):
                        urls.append((u'搜狐新闻', news.text, url,  feed_soup.find('article')))

            if ii==10:
                for news in top_news.find_all('a'):
                    url = news['href']
                    feed_content = opener.open(url).content.decode(self.feed_encoding)
                    feed_soup = BeautifulSoup(feed_content, "lxml")
                    if feed_soup.find('article'):
                        urls.append((u'搜狐IT新闻', news.text, url,  feed_soup.find('article')))      
        return urls
    
