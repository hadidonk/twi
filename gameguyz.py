#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
  采集gameguyz.com站点
'''

from bs4 import BeautifulSoup
import urllib,os,simplejson
from weibo.sinaweibopy.sinaweibo import post_weibo_sina
from weibo.qqweibopy.postqqweibo import post_qq_weibo
from weibo.postweibo import postWeibo
from webthumb.common import *

# Get a file-like object for the Python Web site's home page.
f = urllib.urlopen("http://www.gameguyz.com")
# Read from the object, storing the page's contents in 'html'.
html = f.read()
f.close()
#soup = BeautifulSoup(html)
soup = BeautifulSoup(''.join(html))

params = []
#item = {}
#item['title'] = u'google pic33q'
#item['pic']   = '/home/meadhu/Desktop/173628426.jpg'

# 大眼睛 -- 4
for thumb in soup.find(id="iPThumb").find_all('div'):
  item = {}
  item['title'] = thumb.img["bigtipscontent"]
  item['link']  = generate_short_url(thumb.a["href"])
  item['pic']   = thumb.img["bigsrc"]
  params.append(item)
  
# 右侧新闻 -- 12
for i in soup.find(id="iPFr").find_all("li"):
  item = {}
  item['title'] = i.a['title']
  item['link']  = generate_short_url(i.a['href'])
  item['pic']   = ''
  params.append(item)

# Game Videos -- 5
for i in soup.find_all("table", "game_videos")[0].find_all("td"):
  item = {}
  item['title'] = i.img['alt']
  item['link']  = generate_short_url(i.a['href'])
  item['pic']   = i.img['src']
  params.append(item)

# Game News -- 10
item = {}
game_news = soup.find_all("div","iGameNewsBox")[0].find_all("div","iGNPicBox")[0]
item['title'] = game_news.p.text
item['link']  = generate_short_url(game_news.a['href'])
item['pic']   = game_news.img['src']
params.append(item)
for i in soup.find_all("div","iGameNewsBox")[0].find_all("div","iGNList"):
  item = {}
  item['title'] = i.a['title']
  item['link']  = generate_short_url(i.a['href'])
  params.append(item)

# Game Vendor -- 4, Browser Games -- 3
for i in soup.find_all("div","around_the_network"):
  item = {}
  item['title'] = i.p.text[:140]
  item['link']  = i.a['href']
  item['pic'] = i.img['src']
  params.append(item)

# Pictures -- 6
for i in soup.find_all("table","game_photos")[0].find_all("td"):
  item = {}
  item['title'] = i.img['alt'][:140]
  item['link']  = generate_short_url(i.a['href'])
  item['pic'] = i.img['src']
  params.append(item)

# Flash Games -- 6
#for i in soup.find_all("table","front_flash_game")[0].find_all("td"):
#  item = {}
#  item['title'] = i.img['alt'][:140]+i.a['href']
#  item['pic'] = downLoadImg(i.img['src'])
#  params.append(item)

# Gossips -- 7
item = {}
gossips = soup.find_all("div","iGossips")[0].find("a")
item['title'] = gossips.img['alt'][:140]
item['link']  = generate_short_url(gossips.get('href'))
item['pic'] = gossips.img['src']
params.append(item)
for i in soup.find_all("div","iGossips")[0].find_all("li"):
  item = {}
  item['title'] = i.a.text[:140]
  item['link']  = i.a['href']
  params.append(item)

# Beauty -- 9
for i in soup.find_all("table","gg_friends")[0].find_all("td"):
  item = {}
  item['title'] = i.img['alt'][:140]
  item['link']  = generate_short_url(i.a['href'])
  item['pic'] = i.img['src']
  params.append(item)

if __name__ == '__main__':
  #params = []
  #item = {}
  #item['title'] = u'google pic33q'
  #item['pic']   = '/home/meadhu/Desktop/173628426.jpg'
  #params.append(item)
  #print post_weibo_sina(params)
  #print post_qq_weibo(params)
  ret_params = postWeibo(params)
  #print simplejson.dumps(ret_params, indent=4)
  pass
