#!/usr/bin/env python3

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
    if len(magnets) > 0:
        for magnet in magnets:
            print("片名："+magnet["title"])
            print("大小：" + magnet["size"])
            print("日期：" + magnet["time"])
            print("热度：" + magnet["rank"])
            print("磁链：" + magnet["link"] + "\n")
