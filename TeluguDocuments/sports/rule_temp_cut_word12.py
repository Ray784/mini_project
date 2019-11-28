# -*- coding: utf-8 -*-
import codecs
import os
f = open('sprt15.txt',encoding='utf-8')
with codecs.open("sprt15_rpseudo_out.txt",'w',encoding='utf8')as file2:
    wc = 0
    c = 0
    stl = 0
    for word in f.read().split():
        if word in open('pre1_proc_uoh_dict.txt',encoding='utf-8').read():
            print(word)
            wc += 1
        else:
            l = len(word)
            c = 1
            if l >= 14:
                stl = 7
            elif l < 14 and l >= 10:
                stl  = 5
            elif l < 10 and l >=6:
                stl = 4
            else:
                stl = 0
        while c <= stl:
            str = word[:-c]
            if str in open('pre1_proc_uoh_dict.txt',encoding='utf-8').read():
                s1=str
                wc = wc + 1
                print(s1)
                break
            elif str.endswith('ా'):
                s1 = str[:len('ా')] + 'c'
                if s1 in open('pre1_proc_uoh_dict.txt',encoding='utf-8').read():
                    wc = wc + 1
                    print(s1)
                else:
                    s1 = str[:len('ా')] + 'ి'
                    if s1 in open('pre1_proc_uoh_dict.txt',encoding='utf-8').read():
                        wc = wc + 1
                        print(s1)
                    else:
                        s1 = str[:len('ా')] + 'ు'
                        if s1 in open('pre1_proc_uoh_dict.txt',encoding='utf-8').read():
                            wc = wc + 1
                            print(s1)
            elif str.endswith('ి') or  str.endswith('ిc'):
                s1 = str[:len('ిc')] + 'ు'
                if s1 in open('pre1_proc_uoh_dict.txt',encoding='utf-8').read():
                    wc = wc + 1
                    print(s1)
                else:
                    s1 = str[:len('ిc')] + 'c'
                    if s1 in open('pre1_proc_uoh_dict.txt',encoding='utf-8').read():
                        wc = wc + 1
                        print(s1)
            elif str.endswith('ు') or  str.endswith('ూలు'):
                s1 = str[:len('ిc')] + 'ి'
                if s1 in open('pre1_proc_uoh_dict.txt',encoding='utf-8').read():
                    wc = wc + 1
                    print(s1)
                else:
                    s1 = str[:len('ిc')] + 'c'
                    if s1 in open('pre1_proc_uoh_dict.txt',encoding='utf-8').read():
                        wc = wc + 1
                        print(s1)
            elif str.endswith('ె') or  str.endswith('ే') or str.endswith('ేc'):
                s1 = str[:len('ిc')] + 'ి'
                if s1 in open('pre1_proc_uoh_dict.txt',encoding='utf-8').read():
                    wc = wc + 1
                    print(s1)
                else:
                    s1 = str[:len('ిc')] + 'ు'
                    if s1 in open('pre1_proc_uoh_dict.txt',encoding='utf-8').read():
                        wc = wc + 1
                        print(s1)
                    else:
                        s1 = str[:len('ిc')] + 'c'
                        if s1 in open('pre1_proc_uoh_dict.txt',encoding='utf-8').read():
                            wc = wc + 1
                            print(s1)
            elif str.endswith('ో') or  str.endswith('ో'):
                s1 = str[:len('ిc')] + 'ి'
                if s1 in open('pre1_proc_uoh_dict.txt',encoding='utf-8').read():
                    wc = wc + 1
                    print(s1)
                else:
                    s1 = str[:len('ిc')] + 'ు'
                    if s1 in open('pre1_proc_uoh_dict.txt',encoding='utf-8').read():
                        wc = wc + 1
                        print(s1)
            elif str.endswith('c'):
                s1 = str[:len('c')] + 'ు'
                if s1 in open('pre1_proc_uoh_dict.txt',encoding='utf-8').read():
                    wc = wc + 1
                    print(s1)    
            c += 1
print("iden=",wc)
#print("not identified=",c)

