#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 12:38:44 2021

@author: t08073jc
"""
LINE_AMOUNT = 800
ROW_AMOUNT=600
#Write a text file that is 800 by 600 in G
line=str()
f = open("myfile.txt", "w")
listy=[]
for i in range(LINE_AMOUNT-1):
    line=line+str('G ')
line=line+str("G\n")

for i in range(ROW_AMOUNT):
    listy.append(line)

    
print(listy)

f.writelines(listy)
f.close()