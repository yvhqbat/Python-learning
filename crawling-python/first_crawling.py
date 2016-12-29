#!/usr/bin/python

import urllib2
import re

def download(url):
    "return the html from the url"
    print 'downloading:',url
    try:
        html=urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'download error:',e.reason
        html=None
    return html

def crawl_sitemap(url):
    sitemap=download(url)
    links=re.findall('<loc>(.*?)</loc>',sitemap)
    for link in links:
        print link

def get_links(html):
    "return a list of links from html"
    webpage_regex=re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
    #list of all links from the webpage
    return webpage_regex.findall(html)

def link_crawler(seed_url,link_regex):
    "crawl from the given seed_url following links matched by link_regex"
    crawl_queue=[seed_url]
    while crawl_queue:
        url=crawl_queue.pop()
        html=download(url)
        for link in get_links(html):
            if re.match(link_regex,link):
                crawl_queue.append(link)
            print link


#html=download("http://www.baidu.com")
#print html

url=raw_input('please input the url: ')
##crawl_sitemap(url)

#html=download(url)
#links=get_links(html)
#for link in links:
#    print link

link_crawler('http://example.webscraping.com','/(index|view)')



