# -*- coding: utf-8 -*-
#file="sample1.txt"
import codecs
import os
words = ['డు', 'ము', 'వు', 'లు', 'నిన్', 'నున్', 'లన్', 'కూర్చి', 'గురించి', 'చేతన్', 'చేన్', 'తొడన్', 'తోన్', 'కొఱకున్', 'కై', 'వలనన్', 'కంటెన్', 'పట్టి', 'కిన్', 'కున్', 'యెక్క', 'లోన్', 'లోపలన్', 'అందున్', ' నన్' ,'కి','కు' ,'కె','కై' ,'గా' ,'గాను', 'చే', 'తో','ను','లు', 'ల' ,'లోన' , 'పైన' ,'లతో','ని', 'నికి', 'గాని', 'నుండి' ,'పై', 'నున్న', 'కంటూ', 'మైన' , 'న్నాయి' , 'డం', 'కంటూ', 'స్తాయి', 'లకే', 'లకు', 'లే', 'ది' , 'లం', 'న్ని' , 'నా','న', 'తోనూ', 'ల్లో', 'లో', 'లన్న' ,'వీ', 'లనే', 'కూ','లోకి', 'లాంటి' , 'లైన', 'లుగా', 'ల్ని','చారు', 'ననీ', 'నకు', 'న్నాం', 'చాం' ]
f = open('pre_sprt50.txt',encoding='utf-8')
with codecs.open("sprt50_suff_out.txt",'w',encoding='utf8') as file2:
    wc = 0
#f1 = open('vibha_list.txt',encoding='utf-8')
    for word1 in f.read().split():
        str = word1
        for word in words:
            if str.endswith(word):
                str = str[:-len(word)] + ' '
        if str in open('pre1_proc_uoh_dict.txt',encoding='utf-8').read():
            wc = wc + 1
            file2.write(str)
            file2.write(os.linesep) 
        
print(wc)

