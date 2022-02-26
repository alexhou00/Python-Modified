# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 19:34:49 2022

@author: alexhou00
"""

import sys
import re
from collections import OrderedDict as Dict

map_nums ={u'零':0, u'一':1, u'二':2, u'三':3, u'四':4, u'五':5, u'六':6, u'七':7, u'八':8, u'九':9, u'十':10, u'百':100, u'千':1000, u'万':10000,
       u'０':0, u'１':1, u'２':2, u'３':3, u'４':4, u'５':5, u'６':6, u'７':7, u'８':8, u'９':9,
                u'壹':1, u'贰':2, u'叁':3, u'肆':4, u'伍':5, u'陆':6, u'柒':7, u'捌':8, u'玖':9, u'拾':10, u'佰':100, u'仟':1000, u'萬':10000,
       u'亿':100000000}

def getResultForDigit(a, encoding="utf-8"):
    if isinstance(a, str):
        #a = a.decode(encoding)
        pass

    count = 0 
    result = 0
    tmp = 0
    Billion = 0  
    while count < len(a):
        tmpChr = a[count]
        #print tmpChr
        tmpNum = map_nums.get(tmpChr, None)
        #如果等于1亿
        if tmpNum == 100000000:
            result = result + tmp
            result = result * tmpNum
            #获得亿以上的数量，将其保存在中间变量Billion中并清空result
            Billion = Billion * 100000000 + result 
            result = 0
            tmp = 0
        #如果等于1万
        elif tmpNum == 10000:
            result = result + tmp
            result = result * tmpNum
            tmp = 0
        #如果等于十或者百，千
        elif tmpNum >= 10:
            if tmp == 0:
                tmp = 1
            result = result + tmpNum * tmp
            tmp = 0
        #如果是个位数
        elif tmpNum is not None:
            tmp = tmp * 10 + tmpNum
        count += 1
    result = result + tmp
    result = result + Billion
    return result

dct = Dict()
with open(r"C:\Alex\Python\Python-Modified\Zh-Python\trans_keys.dat",'r',encoding='utf-8') as f:
    for line in f:
        lst = line.strip().split(maxsplit=1)
        if lst != []: dct[lst[0]] = lst[1]
            
dctsub = Dict()
with open(r"C:\Alex\Python\Python-Modified\Zh-Python\sub_keys.dat",'r',encoding='utf-8') as f:
    for line in f:
        lst = line.strip().split('||')
        if lst != []: dctsub[lst[0]] = lst[1]
        
try:
    path = sys.argv[1]
except:
    path = input()
path = path.replace("\\", r"\\")
with open(path,'r',encoding='utf-8') as f:
    f = '\n'.join(f)
    for key, val in dct.items():
        f = f.replace(key, val)
               
for pat, repl in dctsub.items():
    #try:
    #if True:
        if repl.startswith('func_'):
            f = re.sub(pat.replace("\\", r"\\"), eval(repl[5:]), f)
        else:
            f = re.sub(pat, repl, f)
            #print(f)
    #except:
        #print(repl)

#print(f)
exec(f)