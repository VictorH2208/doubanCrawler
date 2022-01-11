# -*- coding = utf-8 -*-
# @Time: 2022-01-02 6:25 p.m.
# @Author: Xinyuan(Victor) Huang
# @File testUrlilb.py
# @Software: PyCharm

import urllib.request

#获取一个get请求
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8')) #对获取的网址源码进行utf-8的解码

#获取一个post请求 检测用httpbin.org
import urllib.parse
# data = bytes(urllib.parse.urlencode({'hello': 'world'}), encoding= 'utf-8')
# response = urllib.request.urlopen("http://httpbin.org/post", data= data)
# print(response.read().decode('utf-8'))

#超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as err:
#     print('timeout')

#网页解析
# response = urllib.request.urlopen("http://www.baidu.com",timeout=1)
# print(response.status) #状态码 418-发现爬虫
# print(response.getheader('Server'))

#爬虫伪装
url = 'http://www.douban.com'
#url = "http://httpbin.org/post"
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}
data = bytes(urllib.parse.urlencode({"name":"eric"}), encoding= 'utf-8')
req = urllib.request.Request(url= url, headers= headers, method= 'POST')
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))