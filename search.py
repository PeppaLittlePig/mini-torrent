#!/usr/bin/env python3
import requests
from lxml import etree
import math
import utils
import re

search_addr = 'https://www.btyunsou.me'

HEADER = {
    "Accept-Encoding":"gzip, deflate, sdch",
    'X-Requested-With': 'XMLHttpRequest',
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}


def run(kw,num):
    '''
    开始抓取资源
    :param kw: 搜索关键字
    :param num: 需要返回的条数
    :return:
    '''
    if num < 0 or num > 100:
        num = 50

    #every page 10 row
    page = int(math.ceil(num / 10))
    for p in range(1,page + 1):
        url = search_addr + "/search/{kw}_ctime_{p}.html".format(kw=kw, p=p)
        try:
            resp = requests.get(url,headers=HEADER).text
            parse(resp,kw,p)
        except Exception as e:
            print(e)

def parse(content,kw,p):
    '''
    解析页面内容
    :param content:
    :param kw:
    :return:
    '''
    html = etree.HTML(content)
    lis = html.xpath('//ul[@class="media-list media-list-set"]/li[@class="media"]')
    if(len(lis) > 0):
        magnets = []
        for li in lis:
            _name = utils.concact_str(li.xpath('.//div[@class="media-body"]//a[@class="title"]/text()'))
            name = True #_name if kw in _name else None  是否需要精准匹配
            if name:
                time = li.xpath('.//div[@class="media-more"]//span[@class="label label-success"]/text()')[0]
                size = li.xpath('.//div[@class="media-more"]//span[@class="label label-warning"]/text()')[0]
                rank = li.xpath('.//div[@class="media-more"]//span[@class="label label-primary"]/text()')[0]
                link_comment = str(li.xpath('.//div[@class="media-more"]//comment()')[0]) #磁力链接在注释里
                flag = re.search(r'<a.*?href="([^"]*)".*?>([\S\s]*?)</a>', link_comment)
                if flag:
                    link = flag.groups()[0]
                    magnets.append({
                        "title":_name,
                        "time":time,
                        "size":size,
                        "rank":rank,
                        "link":link
                    })

        print(magnets)

    else:
        print("页码:"+str(p)+",《"+kw+"》暂无资源 ...")


if __name__ == '__main__':
    run('宝贝计划',10)




