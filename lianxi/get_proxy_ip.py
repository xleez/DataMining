#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import os
import lxml


class get_proxy:
    def proxy(self):
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
        headers = {'User-Agent': user_agent}

        session = requests.session()
        page = session.get('http://www.xicidaili.com/nn/1',headers=headers)
        soup = BeautifulSoup(page.text,'lxml')

        proxylist = []
        taglist = soup.find_all('tr',attrs={
            'class':re.compile("(odd)|()")
            })

        for trtag in taglist:
            tdlist = trtag.find_all('td')
            # print tdlist[1].string   #得到ip地址
            # print tdlist[2].string  #得到端口号
            proxy = {
                # 'http':'http://'+tdlist[1].string + ':' +tdlist[2].string,
                # 'http':'http://'+tdlist[1].string + ':' + tdlist[2].string,
                'http':'http://'+tdlist[1].string + ':' +tdlist[2].string,
                'http':'http://'+tdlist[1].string + ':' + tdlist[2].string,
             }
            print type(proxy)
#测试得到的ip地址能不能用
            url = "http://ip.chinaz.com/getip.aspx"  #用来测试IP是否可用的url
            try:
                 response = session.get(url, proxies=proxy, timeout=5)
                 proxylist.append(proxy)
                 if(len(proxylist) == 10):
                     break
            except Exception,e:
                    continue
            print   proxylist
            return  proxylist



proxy = get_proxy()
proxy.proxy()