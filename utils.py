#!/usr/bin/env python3
import codecs

def concact_str(list):
    '''
    将list拼接成字符串
    :param list:
    :return:
    '''
    result = ''
    for l in list:
        result += l
    return result.strip();

def print_format(magnets):
    '''
    格式化打印
    :param magnets:
    :return:
    '''
    if len(magnets) > 0:
        for magnet in magnets:
            print("片名："+magnet["title"])
            print("大小：" + magnet["size"])
            print("日期：" + magnet["time"])
            print("热度：" + magnet["rank"])
            print("磁链：" + magnet["link"] + "\n")

def save_file(magnets,path):
    '''
    保存至文件
    :param magnets:
    :param path:
    :return:
    '''
    if len(magnets) > 0:
        f = codecs.open(path, 'a', 'utf8')
        for magnet in magnets:
            f.write("片名：" + magnet["title"] +"\r\n")
            f.write("大小：" + magnet["size"] +"\r\n")
            f.write("日期：" + magnet["time"] +"\r\n")
            f.write("热度：" + magnet["rank"] +"\r\n")
            f.write("磁链：" + magnet["link"] + "\r\n")
            f.write("\r\n")

        f.close()

def  getSort(sort):
    if sort == 1:
        return 'length'
    elif sort == 2:
        return 'click'
    else:
        return 'ctime'


