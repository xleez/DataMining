#-*-coding:utf-8-*-
import MySQLdb
connect = MySQLdb.connect(host='localhost',user='root',passwd='199523',
db='mydjangoblog',charset='utf8')
try:
    cursor = connect.cursor()
    sql = 'show tables'
    result = cursor.execute(sql)
    data = cursor.fetchone()
    print result,data
    print 'mysql链接成功'
except:
    print 'mysql链接失败'

