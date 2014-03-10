pm25
===========
* 通过 BeautifulSoup 解析pm2.5网站上的数据
* 只支持Python2


安装
===========

    $ sudo pip install pm25


依赖
===========
BeautifulSoup


使用方法
===========

    >>> import pm25
    >>> print pm25.get('beijing')['time']
    更新：03-10 10:00 
    >>> print pm25.get('beijing')['AQI']
    [u'114', u'102', u'102', u'93', u'89', u'97', u'99', u'104', u'95', u'74', u'67', u'77', u'97']
    >>> print pm25.get('beijing')[u'监测点'][0]
    美国大使馆


返回值结构
===========
* time —— 字符串；数据发布时间
* 监测点 —— 字符串列表；所有监测点，注意获取数据时候要加u，比如`pm25.get('beijing')[u'监测点']`
* AQI —— 字符串列表；所有监测点对应的AQI
* 质量状况 —— 字符串列表；所有监测点对应的质量状况
* PM2.5浓度 —— 字符串列表；所有监测点对应的PM2.5浓度
* now —— 字符串；当前空气质量


协议
===========
基于[WTFPL](http://en.wikipedia.org/wiki/WTFPL)协议开源。
