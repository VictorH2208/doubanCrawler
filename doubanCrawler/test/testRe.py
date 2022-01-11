# -*- coding = utf-8 -*-
# @Time: 2022-01-03 4:52 p.m.
# @Author: Xinyuan(Victor) Huang
# @File testRe.py
# @Software: PyCharm

#正则表达式：字符串模式（判断字符串是否符合一定的标准）
import re

#创建模式对象
# pat = re.compile('AA') #此处AA是正则表达式，用来去验证其他的字符串
# m = pat.search('CBA') #search字符串被校验的内容
# m = pat.search('ACBAA')
# m = pat.search('AACBAACBA')

#没有模式对象
# m = re.search('asd', 'Aasd') #前面的字符串是规则，后面的是对象
#
# print(m)

#findall
# print(re.findall('a', 'ASDaDFGAa')) #前面是规则，后面是对象
print(re.findall('[A-Z]', 'ASDaDFGAa'))
print(re.findall('[A-Z]+', 'ASDaDFGAa'))

#sub

print(re.sub('a', 'A', 'abcdcasd')) #找到a用A替换

#建议在正则表达是中，被比较的字符串前面加上r，不用担心转义字符的问题
a = r"\aabd-\'"
print(a)

