# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:14:36 2020

@author: Mayra
"""
import bs4
from  bs4 import BeautifulSoup as bs
from urllib.request import urlopen

news_url = "https://news.google.com/news/rss"
Client = urlopen(news_url)
xml_page=Client.read()
Client.close()
soup_pages=bs(xml_page,"html5lib")
news_list=soup_pages.find_all("item")
for news in news_list:
    print(news.title.text)
    print(news.link.text)
    print(news.pubDate.text)
    print("-"*60)
