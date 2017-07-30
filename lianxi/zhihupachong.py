#-*- coding:utf-8 -*-
import requests
import os
import cookielib
from httplib import *
import json
import lxml
from bs4 import BeautifulSoup
import get_proxy_ip

#代理ip地址
proxy_ip = get_proxy_ip.get_proxy()
get_ip = proxy_ip.proxy()
proxies = get_ip

headers = {
    'Referer': 'http://www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',
    'Connection':'keep-alive',
    'Accept-Encoding':'gzip, deflate, br',
    "Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
    'Host':'www.zhihu.com',
    'Accept':'*/*',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
}



#使用cookie信息登陆
session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True)
except:
    print 'cookie未能找到'



#获得验证码
def get_yanzhengma():
    yanzhengma_url = 'https://www.zhihu.com/captcha.gif?r=1491186578975&type=login'
    yanzhengma_image_content = requests.get(url=yanzhengma_url,headers=headers).content
    with open(os.getcwd()+'/'+'1.gif', 'wb') as wf:
        wf.write(yanzhengma_image_content)
    yanzhengma = raw_input('验证码:')
    return yanzhengma


#获得_xsrf
def get_xsrf():
    xsrf_url = 'https://www.zhihu.com/#signin'
    xsrf_html = requests.get(url=xsrf_url,headers=headers).text
    soup = BeautifulSoup(xsrf_html,'lxml')
    getxsrf = soup.find('input',attrs={'name':'_xsrf'}).get("value")
    return getxsrf



#验证是否登陆成功
def islogin():
    isurl = 'https://www.zhihu.com/settings/profile'
    login_code = session.get(url=isurl,allow_redirects=False).status_code
    if int(x=login_code)==200:
        return True
    else:
        return False



#登陆知乎
def login(email,password):
    print '邮箱登陆'
    post_url = 'https://www.zhihu.com/#signins/eamil'
    post_data = {
        '_xrsf': get_xsrf(),
        'pasword':password,
        'captcha':get_yanzhengma(),
        'eamil': email,
    }
    response = session.post(url=post_url,data=post_data,headers=headers,proxies=proxies)
    login_code = response.content
    print response.status_code
    print login_code
    for i in session.cookies:
        print i
    session.cookies.save()

    if __name__ == '__main__':
        if islogin():
            print '你已经登陆'
        else:
            print '登陆失败'

if __name__ == '__main__':
    # email = raw_input('输入邮箱：')
    # password = raw_input('输入密码：')
   # login(email=email,password=password)
    login(email='yiqunlinux@163.com',password='arvinghibli.top')



