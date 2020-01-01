import codecs
import os
import string as String
no_max = 0
no_mid = 0
no_sml = 0
files=os.listdir()
for file in files:
    file1 = open(file,"r",encoding="utf-8")
    if not '.txt' in file:
        continue
    with codecs.open('log','w',encoding='utf8') as log:
        with codecs.open('T'+file,'w',encoding='utf8') as file2:
            stringTotal = file1.read()
            exclude = set(String.punctuation)
            stringTotal = ''.join(ch for ch in stringTotal if ch not in exclude)
            stringList = stringTotal[:-1].split(' ')
            for string in stringList:
                    list1 = []
                    while string!="":
                            log.write('\n8787\n')
                            log.write(string)
                            log.write('\n')
                            c = 1
                            str1=codecs.encode(bytes(string,'utf-8'),'hex')
                            str1 = str(str1)
                            str1=str(str1[:-1])
                            str1=str(str1[2:])
                            print(str1)
                            if str(str1[-6:])=='e0b082':
                              str1=str(str1[:-6])
                              c+=1
                            str5=str(str1[-6:])
                            str3=str(str1[:-6])
                            print(str5)
                            print(str3)
                            a = ['b1','b0bf','b0be']
                            if any(x in str5 for x in a):
                                    c+=1
                                    str5=str1[:-12]
                                    while True:
                                            str4=str5[-6:]
                                            #print str4
                                            if str4 =='e0b18d':
                                                    c+=2
                                            else:
                                                    break
                                            str5=str5[:-6]	
                            elif str3[-6:]=='e0b18d':
                                    str3=str3[:-12]
                                    c+=2
                                    while True:
                                            str6=str3[-6:]
                                            if 	str6=='e0b18d':
                                                    c+=2
                                            else:
                                                    break
                                            str3=str3[:-12]		
                            log.write(str1+' \n')
                            log.write(string+'\n')
                            log.write(str(c)+'\n')
                            print(string)
                            print(c)		
                            str2 = string[-c:]
                            string = string[:-c]
                            string = string
                            string1 = str2
                            print(string1)
                            log.write(string1+'\n')
                            print(len(string1))
                            list1.append(string1)
                            print(list1)
                    count=0
                    for i in reversed(list1):
                            file2.write( i )
                            count+=1
                            if(count==3):
                                break
                    # log.write('\n')
                    # file2.write('---%d' % cn)
                    # file2.write(os.linesep)
                    file2.write(' ')
                    
        #http://www.utf8-chartable.com/unicode-utf8-table.pl?start=3072&number=128
