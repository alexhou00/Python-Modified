# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 17:41:58 2022

@author: alexhou00
"""
import sys

dct = dict()
with open(r"C:\Alex\Python\Python-Modified\Python-Boshiamy\boshiamy.dat",'r',encoding='utf-8') as f:
    for line in f:
        lst = line.split()
        if lst[1] in dct:
            if len(dct[lst[1]]) > len(lst[0]): dct[lst[1]] = lst[0]
        else:
            dct[lst[1]] = lst[0]
            
txt = ''    
path = sys.argv[1]
path = path.replace("\\", r"\\")
with open(path,'r',encoding='utf-8') as f:
    #ft = tuple(f)
    for line in f:
        for char in line:
            if char in dct:
                txt += char.replace(char, dct[char])
            elif char == '　':
                txt+=' '
            else:
                txt+=char
                
                
txt = txt.replace('vfio','==')
exec(txt)