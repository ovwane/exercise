#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
Created on 2017年8月21日

@author: li tao
"""

f = open('H:\\project\\Nidone_appium\\log\\2017-08-28_17_24_05.log')
data = f.readlines()
for i in range(0, len(data)-1):
    if '登录测试' in data[i]:
        r = open('H:\\project\\Nidone_appium\\log\\321.log', 'w+')
        for j in range(i, len(data)-1):
            r.writelines(data[j])
        r.close()