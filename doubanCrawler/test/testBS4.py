# -*- coding = utf-8 -*-
# @Time: 2022-01-03 3:03 p.m.
# @Author: Xinyuan(Victor) Huang
# @File testBS4.py
# @Software: PyCharm

'''
BeautifulSoup4将复杂html文档转换成一个复杂的树形结构，每个节点都是python对象，所有节点可以归为
-tag
-navigable string
-beautiful soup
-comment
'''

from bs4 import BeautifulSoup

file = open("./baidu.html", 'rb') #二进制读取
html = file.read()
bs = BeautifulSoup(html,'html.parser')

# print(bs.title) #找到第一个
# print(bs.a)
# print(bs.head)

# print(type(bs.head))
# 1. Tag 标签及其内容：拿到所找到的第一个内容

# print(bs.title.string)
# print(bs.a.attrs)
#2.NavigableString 标签里的内容（字符串）

# print(type(bs))
# print(bs.name)
# print(bs)
#3.BeautifulSoup 表示整个文档

# print(bs.a.string)
# print(type(bs.a.string))
#4.Comment 是一个特殊的NavigableString

#--------------------------------------------------------------

#文档遍历
#更多内容搜索BeautifulSoup文档

#print(bs.head.contents)
#print(bs.head.contents[1])


#文档搜索

#(1)find_all()
t_list = bs.find_all('a')
# print(t_list)

import re
#正则表达式搜索：使用search（）方法来匹配内容
# t_list = bs.find_all(re.compile(('a'))) #只要含有a
# print(t_list)

#方法：传入一个函数（方法），根据函数的要求来搜索
# def name_is_exists(tag):
#     return tag.has_attr('name')
#
# t_list = bs.find_all(name_is_exists)
#
# for item in t_list:
#     print(item)


#(2)kwargs 参数
# t_list = bs.find_all(id= 'head')
# t_list = bs.find_all(class_=True)
# t_list = bs.find_all(href='http://news.baidu.com')
# for item in t_list:
#     print(item)

#(3)text参数
# t_list = bs.find_all(text= 'hao123')
# t_list = bs.find_all(text = ['hao123', '地图', '贴吧'])
# t_list = bs.find_all(text = re.compile('\d')) #应用正则表达式来查找包含特定文本的内容（标签里的字符串）
# for item in t_list:
#     print(item)

#(4)limit参数
# t_list = bs.find_all('a', limit = 3)
# for item in t_list:
#     print(item)

#(5)css选择器
# t_list = bs.select('title') #通过标签来查找
# t_list = bs.select('.mnav') #通过类名查找
# t_list= bs.select('#u1') #通过id查找
# t_list = bs.select('a[class="bri"]') #通过属性查找
# t_list = bs.select('head > title') #通过子标签查找
t_list = bs.select('.mnav ~ .bri')
print(t_list[0].get_text())

# for item in t_list:
#     print(item)










