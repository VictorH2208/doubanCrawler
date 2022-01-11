# -*- coding = utf-8 -*-
# @Time: 2022-01-05 3:05 p.m.
# @Author: Xinyuan(Victor) Huang
# @File testSqlite.py
# @Software: PyCharm

import sqlite3

#1.连接数据库
# conn = sqlite3.connect('test.db') #打开或创建数据库文件
#
# print('Opened Database Successfully')

conn = sqlite3.connect('test.db') #打开或创建数据库文件

print('成功打开数据库')

#2.创建数据表
# c = conn.cursor() #获取游标
#
# sql = '''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real);
# '''
#
# c.execute(sql) #执行sql语句
# conn.commit() #提交数据库操作
# conn.close() #关闭数据库连接
#
# print('建表成功')

#3.插入数据
# c = conn.cursor() #获取游标
#
# sql1 = '''
#     insert into company (id,name,age,address, salary)
#     values(1,'张三',32, "成都",8000);
# '''
# sql2 = '''
#     insert into company (id,name,age,address, salary)
#     values(2,'李四',32, "重庆",15000);
# '''
#
# c.execute(sql1) #执行sql语句从
# c.execute(sql2)
# conn.commit() #提交数据库操作
# conn.close() #关闭数据库连接
#
# print('插入成功')

#4.查询数据
c = conn.cursor() #获取游标

sql1 = 'select id,name,address,salary from company'

cursor = c.execute(sql1) #执行sql语句从

for row in cursor:
    print('id = ', row[0])
    print('name = ', row[1])
    print('address = ',row[2])
    print('salary = ', row[3])

print('查询成功')