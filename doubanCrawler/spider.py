# -*- coding = utf-8 -*-
# @Time: 2022-01-02 3:18 p.m.
# @Author: Xinyuan(Victor) Huang
# @File spider.py
# @Software: PyCharm

import urllib.request, urllib.error   #制定url，获取网页数据
import re       #正则表达式，文字匹配
from bs4 import BeautifulSoup     #网页解析
import xlwt     #excel操作
import sqlite3  #数据库操作

def main():
    baseurl = "https://movie.douban.com/top250?start="
    #1. 爬取网页
    datalist = getData(baseurl)

    #3. 保存数据
    #savepath = "./豆瓣电影Top250.xls"
    #saveData(datalist, savepath)
    dbpath = 'movie.db'
    saveData2DB(datalist, dbpath)

#影片详情规则
findLink = re.compile(r'<a href="(.*?)">') #创建正则表达式对象，表示规则
#影片图片
findImage = re.compile(r'<img.*src="(.*?)"', re.S)
#片名
findTitle = re.compile(r'<span class="title">(.*?)</span>')
#评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
#评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#影片概况
findInq= re.compile(r'<span class="inq">(.*)</span>')
#相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)

#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(10):  #调用过去页面信息的函数，10次
        url = baseurl + str(i*25)
        html = askURL(url) #保存获取到的网页源码

        # 2. 逐一解析网页
        soup = BeautifulSoup(html, 'html.parser')
        for item in soup.find_all('div', class_= 'item'): #查找符合要求的字符串，形成列表
            data = [] #一部电影的信息
            item = str(item)

            #影片详情链接获取
            link = re.findall(findLink, item)[0] #re库通过正则表达式查找指定的字符串
            data.append(link) #添加链接

            imgSrc = re.findall(findImage,item)[0]
            data.append(imgSrc) #添加图片

            titles = re.findall(findTitle, item) #片名可能只有一个中文名灭有英文名
            if(len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle) #添加中文名
                otitle = titles[1].replace("/", '') #去掉无关符号
                data.append(otitle) #添加外国名
            else:
                data.append(titles[0])
                data.append(' ') #外国名留空

            rating = re.findall(findRating, item)[0]
            data.append(rating) #添加评分

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum) #添加评价人数

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace('。', "") #去掉句号
            else:
                inq = ""
            data.append(inq) #添加概述

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', ' ', bd)
            bd = re.sub('/', ' ', bd)
            data.append(bd.strip())

            datalist.append(data)

    return datalist

#得到指定一个url的网页内容
def askURL(url):
    head = { #模拟头部信息像豆瓣服务器发送消息
        "User-Agent" : "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 96.0.4664.110 Safari / 537.36"
    }
                #用户代理，表示告诉豆瓣服务器我们是什么类型的机器，浏览器 （本质是告诉服务器能够接受什么格式的信息）
    request = urllib.request.Request(url, headers= head)
    html = ''
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        #print(html)
    except urllib.error.URLError as err:
        if hasattr(err, 'code'):
            print(err.code)
        if hasattr(err, 'reason'):
            print(err.reason)

    return html

#保存数据
def saveData(datalist, savepath):
    print("Saved")
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)  # 创建工作表
    col = ('电影详情链接','图片链接','中文名','外文名','评分','评价数','概况','相关信息')
    for i in range(8):
        sheet.write(0,i,col[i]) #列名
    for i in range(250):
        print('第%d条'%(i+1))
        data = datalist[i]
        for j in range(8):
            sheet.write(i+1,j,data[j])

    book.save(savepath)  # 保存数据表

def saveData2DB(datalist,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"'+data[index]+'"'
        sql = '''
            insert into movieTop250 (
            info_link,pic_link,cname,ename,score,rated,introduction,info)
            values(%s)'''%",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()

def init_db(dbpath):
    sql = '''
        create table movieTop250 
        (id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rated numeric,
        introduction text,
        info text);
    ''' #创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
    print('爬取完毕')
