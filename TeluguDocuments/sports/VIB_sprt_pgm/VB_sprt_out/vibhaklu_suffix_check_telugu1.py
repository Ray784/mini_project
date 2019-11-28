# -*- coding: utf-8 -*-
#file="sample1.txt"
import codecs
import os
wc = 0
c = 0
words = [ 'డు', 'ము', 'వు', 'లు', 'నిన్', 'నున్', 'లన్', 'కూర్చి', 'గురించి', 'చేతన్', 'చేన్', 'తొడన్', 'తోన్', 'కొఱకున్', 'కై', 'వలనన్', 'కంటెన్', 'పట్టి', 'కిన్', 'కున్', 'యెక్క', 'లోన్', 'లోపలన్', 'అందున్', ' నన్' ]
f = open('pre_sprt50.txt',encoding='utf-8')
with codecs.open("sprt50_vib_out.txt",'w',encoding='utf8') as file2:
#f1 = open('vibha_list.txt',encoding='utf-8')
    for word1 in f.read().split():
        c = c + 1
        str = word1
        for word in words:
            if str.endswith(word):
                str = str[:-len(word)] + ' '
        if str in open('pre1_proc_uoh_dict.txt',encoding='utf-8').read():
            file2.write(str)
            file2.write(os.linesep)
            wc = wc + 1
                    
print(wc)
print(c)
