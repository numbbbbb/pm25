#!/usr/bin/env python
# coding:utf-8

import urllib
from bs4 import BeautifulSoup
import re
import json
import os
import functools


def cache(func):
    """cache the value in memory
    """
    table = func.cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = '{0}{1}'.format(args, kwargs)
        if key not in table:
            table[key] = func(*args, **kwargs)
        return table[key]
    return wrapper


@cache
def _get_pm25_data(city):
    """get pm2.5 data per hour for every city
    """
    html_doc = urllib.urlopen('http://m.cnpm25.cn/pm/%s.html' % (city, )).read().decode('utf-8')
    soup = BeautifulSoup(html_doc)
    tempdata = []
    alldata = {}

    try:
        if "url" in soup.html.head.prettify():
            urllib.urlopen(soup.html.head.meta['content'].split(";")[1][4:])
            html_doc = urllib.urlopen('http://m.cnpm25.cn/pm/%s.html' % (city, )).read().decode('utf-8')
            soup = BeautifulSoup(html_doc)
    except:
        pass

    for x in soup.find_all('div', 'dl1'):
        try:
            x.img.extract()
        except:
            pass
        tempdata.append(x.string)
    alldata[tempdata[0]] = []
    alldata[tempdata[1]] = []
    alldata[tempdata[2]] = []
    for i in range(3, len(tempdata[3:]), 3):
        alldata[tempdata[0]].append(tempdata[i])
        alldata[tempdata[1]].append(tempdata[i + 1])
        alldata[tempdata[2]].append(tempdata[i + 2])

    tempdata = []
    for x in soup.find_all('div', 'dl2'):
        try:
            x.img.extract()
        except:
            pass
        tempdata.append(x.string)
    alldata[tempdata[0]] = tempdata[1:]

    twothings = soup.find_all('div', 'main_aqi')
    twothings[0].div.span.extract()
    alldata['now'] = twothings[0].div.string

    twothings[1].font.script.extract()
    alldata['time'] = twothings[1].font.string
    return alldata


def get(city):
    if city:
        try:
            return _get_pm25_data(city)
        except:
            return '错误： 请检查您是否拼错城市'
