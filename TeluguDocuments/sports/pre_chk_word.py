# -*- coding: utf-8 -*-
import codecs
import os
a = "!.-?,'()0123456789+-/*[]ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
#a = ' " @ '
f = open('sprt50.txt',encoding='utf-8')
wc = 0 
with codecs.open("pre_sprt50.txt",'w',encoding='utf8')as file2:
    for word in f.read().split():
        for char in a:
            word = word.replace(char,"")
            if char == '"':
                word = word.replace(char,"")            
        file2.write(word)
        wc = wc + 1
        file2.write(os.linesep)
print(wc)
        
