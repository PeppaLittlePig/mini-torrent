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