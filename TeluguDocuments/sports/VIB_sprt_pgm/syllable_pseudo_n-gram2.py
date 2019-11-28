import codecs
import os
import string
word =" "
wc=0
file1 = open("sprt2.txt","r",encoding="utf-8")
with codecs.open("sprt2_pseudo_out.txt",'w',encoding='utf8') as file2:
        stringTotal = file1.read()
        exclude = set(string.punctuation)
        stringTotal = ''.join(ch for ch in stringTotal if ch not in exclude)
        stringList = stringTotal[:-1].split(' ')
        for string in stringList:
                list1 = []
                list2 = []
                #string =string[:-1]
                #print string
                while string!="":
                        c = 1
                        str1=codecs.encode(bytes(string,'utf-8'),'hex')
                        #print(str1)
                        str1 = str(str1)
                        str1=str(str1[:-1])
                        str1=str(str1[2:])
                        #print(str1)
                        if str(str1[-6:])=='e0b082':
                          str1=str(str1[:-6])
                          c+=1
                        str5=str(str1[-6:])
                        str3=str(str1[:-6])
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
                        #print c		
                        str2 = string[-c:]
                        string = string[:-c]
                        string = string
                        string1 = str2
                        list1.append(string1)
                #print(list1)
                list2=list1[::-1]
                while len(list2) != 0:
                    word = ''.join(list2)
                    if word in open('pre1_proc_uoh_dict.txt',encoding='utf-8').read():
                        file2.write(word)
                        file2.write(os.linesep)
                        wc+=1
                        break
                    else:
                        list2=list2[:-1]
print("tot=",wc)
                
                
                    
