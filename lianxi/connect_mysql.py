#-*- coding:utf-8 -*-

import pymysql
#连接数据库
connectmysql = pymysql.connect(host='localhost',
port = 3306,user='root',passwd = '199523',
db='mydjangoblog',charset = 'utf8',
                               )
#创建游标
cursor = connectmysql.cursor()
#判断是否连接成功
try:
    with connectmysql.cursor() as cursor:
        #执行mysql语句
        sql = 'show tables'
        cursor.execute(sql)
        connectmysql.commit()
        print cursor.fetchone()
        print 'mysql连接成功'
except:
    print('连接mysql失败')
finally:
    connectmysql.close()
