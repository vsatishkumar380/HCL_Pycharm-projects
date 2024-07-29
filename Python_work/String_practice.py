#whether the string is Symmetrical or Palindrome

#Method1
# strn=input("Enter string to verify:")
# sym_strn=strn[::-1]
# if sym_strn==strn:
#     print("Given string is palandrome.")
# else:
#     print("Given string is not a palandrome.")

#Method2

# strn=input("Enter string to verify:")
# leth_strn=len(strn)
# ls=[]
# while leth_strn>0:
#     val=strn[leth_strn-1]
#     ls.append(val)
#     leth_strn=leth_strn-1
# new_strn="".join(ls)
# print(new_strn)
# if strn==new_strn:
#     print("Given string is palandrome.")
# else:
#     print("Given string is not a palandrome.")

#Method3
# strn=input("Enter string to verify:")
# leth_strn=len(strn)
# new_strn=""
# while leth_strn>0:
#     val=strn[leth_strn-1]
#     new_strn=new_strn+val
#     leth_strn=leth_strn-1
# print(new_strn)
# if strn==new_strn:
#     print("Given string is palandrome.")
# else:
#     print("Given string is not a palandrome.")

'''Reverse Words in a Given String in Python'''

#name=input("Enter the word:")
# def reverse_name(name):
#     len_name=len(name)
#     new = ""
#     for x in name:
#         val=name[len_name-1]
#         new=new+val
#         len_name=len_name-1
#     return new
#
# new_name=reverse_name(name)
# print(new_name)


# word="geeks quiz practice code"
# new_word=word.split()
# val=-1
# s=""
#
# for x in new_word:
#     if val==-1:
#         s=s+new_word[val]
#         val=val-1
#     else:
#         s = s + " " +new_word[val]
#         val = val - 1
# print(s)

# def reverse_line(word):
#     new_word = word.split()
#     val = -1
#     s = ""
#
#     for x in new_word:
#         if val == -1:
#             s = s + new_word[val]
#             val = val - 1
#         else:
#             s = s + " " + new_word[val]
#             val = val - 1
#     print(s)


#
# reverse_line(word)

# word="geeks quiz practice code and my name is laxmi"
# def reverse_method(word):
#     ls=word.split()
#     new_ls=ls[::-1]
#     rever_text=" ".join(new_ls)
#     print(rever_text)
# reverse_method(word)

#How to Remove Letters From a String in Python
# word="Geeks123For123Geeks"
# val=word.count("123")
# new_st=""
# print(val)
# for x in range(val):
#     new_st=word.replace("123","")
#     word=new_st
# print(new_st)

#Find length of a string in python
# word="Geeks123For123Geeks"
# print(len(word))
# sum=0
# for x in word:
#     sum=sum+1
# print(sum)

# def lenth(word):
#     sum = 0
#     for ele in word:
#         sum=sum+1
#     return sum
# val=lenth(word)
# print(val)


#Avoid Spaces in string length
# word="geeksforgeeks 33 best"
# print(len(word))
# sum=0
# for x in word:
#     if x ==" ":
#         pass
#     else:
#         sum=sum+1
# print(sum)
# sum=0
# def avoid_space(word):
#     global sum
#     for x in word:
#         if x==" ":
#             pass
#         else:
#             sum=sum+1
#     return sum
#
# val=avoid_space(word)
# print(val)


#Python program to print even length words in a string

# word="This is a python language and Using the lambda function"
# ls=word.split()
# new_lst=[]
# for x in ls:
#     if len(x)%2==0:
#         new_lst.append(x)
# print(" ".join(new_lst))

# word="geeksforgeeks"
# print(len(word))
# val=len(word)//2
# new=word[:val].lower()+word[val:len(word)].upper()
# print(new)


# word="hello world welcome to geeksforgeeks"
# ls=[]
# for x in word.split():
#     val=len(x)
#     new=x[0].upper()+x[1:val]
#     ls.append(new)
#
# new_word=" ".join(ls)
# print(new_word)

# new_word=word.title()
# print(new_word)

# def string_check(word):
#     is_flag1=False
#     is_flag2=False
#
#     for x in word:
#         if x in "abcdefghigklmnopqrstuvwxyz":
#             is_flag1 = True
#         if x in "0123456789":
#             is_flag2 = True
#     return is_flag1 and is_flag2
#
# word="thishasboth29s"
#
# val=string_check(word)
# print(val)



#Python Program to Accept the Strings Which Contains all Vowels
# word='ABeeIghiObhkUul'
# vowels="aeiou"
# str=""
# for x in vowels:
#     if x in word.lower():
#         pass
#     else:
#         str=str+x
# if str =="":
#     print("given string is Acceptted")
# else:
#     for i in str:
#         print(i,":vowel is not present")
#     print("given string is Rejected")

#Count the Number of matching characters in a pair of string

# str1="aabcddekll12@"
# str2='bb2211@55k'
#
# for x in str1:
#     if x in str2:
#         print(x,end=" ")

#Python program to count number of vowels using sets in given string

# word="PythonStringExercise"

# def count_vowels(word):
#     sum=0
#     vowels="aeiou"
#     for x in word.lower():
#         if x in vowels:
#             sum +=1
#     print("No. of vowels :",sum)
#
# count_vowels(word)
# vowels="aeiou"
# ls=[chr for chr in word.lower() if chr in vowels]
# print(len(ls),ls)

# word="geeksforgeeks"
# strn=""
# for x in word:
#     if x in strn:
#         pass
#     else:
#         strn=strn+x
# print(strn)
#Least Frequent Character in String

# word="GeeksforGeeks"
# strn=""
# ls=[]
# for x in word.lower():
#     if x in strn:
#         pass
#     else:
#         val=word.lower().count(x)
#         ls.append((x,val))
#         strn=strn+x
# print(ls)
# val=0
# # for x,y in ls:
# #     if y>val:
# #         val=y
# # for x,y in ls:
# #     if y==val:
# #         print(x)
# for x,y in ls:
#     if y%2!=0:
#         print(x)


#Frequency of numbers in String

# word="geeks4fee3ks 5is No. 1 4 gee45ks"
# num_strn="0123456789"
# numeric=0
# for x in word:
#     if x in num_strn:
#         numeric +=1
# print(numeric)

# Find words which are greater than given length k

# line="hello geeks for geeks is computer science portal"
# strn=""
# for x in line.split():
#     val=len(x)
#     if val >=4:
#         strn=strn+" "+x
#
# print(strn)
# print(strn[1:])

#Python program to split and join a string
#splict
# word="Import the re module for regular expression operations "
# ls=[]
# strn=""
# for x in word.strip():
#     if x == " ":
#         ls.append(strn)
#         strn=""
#     else:
#         strn=strn+x
# ls.append(strn)
# print(ls)

#Join
# ls=['Geeks', 'for', 'Geeks']
# val=len(ls)
# strn=""
# for x in range(val):
#     if x==0:
#         strn=strn+ls[x]
#     else:
#         strn=strn+"-"+ls[x]
# print(strn)

#Check if a given string is binary string or not
# word="01010101010as"
# out="01"
# is_flag=True
# for x in word:
#     if x in out:
#         is_flag=True
#     else:
#         is_flag=False
# if is_flag == True:
#     print("accept")
# else:
#     print("not accept")


# word='01010101010'
# print(word) 0b,0o 1 to 9,0b a to f, 1 t0 7.

from difflib import get_close_matches


# lst=['ape', 'apple', 'appl','peach', 'puppy']
# word="apple"
# flag = False
# ls=[]
# for x in lst:
#     for y in x:
#         if y in word:
#             flag = True
#         else:
#             flag=False
#             break
#     if flag==True:
#         ls.append(x)
# print(ls)

#Python program to find uncommon words from two Strings

# B = "Geeks for Geeks"
# A = "Learning from Geeks for Geeks"

# val1=len(A)
# val2=len(B)
# ls=[]
# if val1<val2:
#     for x in B.split():
#         if x in A.split():
#             pass
#         else:
#             ls.append(x)
# else:
#     for y in A.split():
#         if y in B.split():
#             pass
#         else:
#             ls.append(y)
# print(ls)


#Python | Swap commas and dots in a String

# word="14,625,498.002"
# strn=""
# for x in word:
#     if x==",":
#         strn=strn+"."
#     elif x==".":
#         strn = strn + ","
#     else:
#         strn=strn+x
# print(strn)


#Permutation of a given string using inbuilt function
# from itertools import permutations
# word="ABC"
#
# perlst=permutations(word)
# for x in perlst:
#     new="".join(x)
#     print(new)

# strn="My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/"
# print(strn.split())
# ls=[]
# for x in strn.split():
#     if x.startswith("https") or x.startswith("http"):
#         ls.append(x)
# print(ls)

code = """ a = 6+5
           print(a)"""
# def exe_code():
#     code="""
# a="abcde"
# for x in a:
#     print(x)
# """
#     exec(code)
#
# exe_code()

# word= 'zero four zero one seven six nine satheesh'
# lst=['zero','one','two','three','four','five','six','seven','eight','nine']
# str=''
# ls=[]
# for x in word.split():
#     if x==lst[0]:
#         ls.append("0")
#     elif x==lst[1]:
#         ls.append("1")
#     elif x==lst[2]:
#         ls.append("2")
#     elif x==lst[3]:
#         ls.append("3")
#     elif x==lst[4]:
#         ls.append("4")
#     elif x==lst[5]:
#         ls.append("5")
#     elif x==lst[6]:
#         ls.append("6")
#     elif x==lst[7]:
#         ls.append("7")
#
#     elif x==lst[8]:
#         ls.append("8")
#     elif x==lst[9]:
#         ls.append("9")
#
#     else:
#         ls.append(x)
# new="".join(ls)
# print(new)

# word="geeksforgeeks is best for geeks"
# check="best"
# sum=0
# if check in word:
#     for x in word.split():
#         sum=sum+1
#         if x == check:
#             break
#     print(sum)
# else:
#     print(" the coun is zero")


# word="geekksforgggeeks"
# sum=1
# ls=[]
# for ele in range(len(word)):
#     if


# word="GeeksforGeeks"
# d=5
# right_new=word[d:len(word)-d]+word[:d]
# print(right_new)

# strn="GEEGEEKSKSwertdff"
# sub_str="GEEKS"
# flag=True
# while len(strn)>=len(sub_str):
#     if strn=="":
#         flag=True
#         break
#     elif sub_str in strn:
#         strn=strn.replace(sub_str,"")
#     else:
#         flag=False
#         break
#
# if flag==True:
#     print('yes')
# else:
#     print('no')

#Python Program to find minimum number of rotations to obtain actual string
# word="geeks"
# val=word.find("g")
# print(val,len(word))
# strn=word[val:len(word)]+word[0:val]
# print(strn)

# def code_exwc():
#     code='''
# a=5
# b=6
# c=a+b
# print(c)
# '''
#     exec(code)
#
# code_exwc()
#
# word='Gfg Gfg Gfg Gfg is best'
# dic={}
# for x in set(word.split()):
#     val=word.count(x)
#     dic[x]=val
#
# print(dic)

#Successive Characters Frequency

# ls=['geekforgeekss','is','bessst','for','geeks']
# lst=[]
# lst1=[]
# for x in ls:
#     val=x.count('s')
#     lst1.append((x,val))
#     lst.append(val)
# print(lst1)
# print(lst)
# lst.sort()
# print(lst)
#
# for x,y in lst1:





# word='geeksforgeeks_is_best'
# strn=""
# for x in word.split("_"):
#     strn=strn+x.title()
# print(strn)

# lst=[5,6,3,1,0,4,8,9,7,2,1]
# lst.sort()
# print(lst)

# ls=['geekforgeeks','is','bessst','for','geeks']
# strn="".join(ls)
# print(strn)
# k=24
# ls1=[]
#
#
# for x in ls:
#     val=len(x)
#     ls1.append(val)
# print(ls1)
# sum=0
# val=0
# for x in ls1:
#     sum=sum+x
#     if sum < k:
#         val=val+1
#
#     else:
#         print(val)
#         break
# ind=val
# print(ls[ind])

# new="GFGaBstuforigeeks"
# vowels="aeiouAEIOU"
# strn=''
# ls=[]
# for x in new:
#     if x in vowels:
#         if strn=="":
#             pass
#         else:
#             ls.append(strn)
#             strn=''
#     else:
#         strn=strn+x
# ls.append(strn)
# print(ls)
# print("".join(ls))



# ls=['gfg', ' ', ' ', 'is', '         ', 'best']
# strn='    '
# new=[]
# flag=True
# for x in ls:
#     for ele in x:
#         if ele not in strn:
#             flag=True
#         else:
#             flag=False
#     if flag==True:
#         new.append(x)
# print(new)





# ls=['allx', 'lovex', 'gfg', 'xit', 'is', 'bestx']
# new=[]
# for x in ls:
#     if x[-1]=="x":
#         pass
#     else:
#         new.append(x)
# print(new)


# ls=[5,3,2,6,9,7,1,4,8,0]
# ls1=[]
# ind=0
# for x in range(len(ls)):
#     val=max(ls)
#     ind=ind-1
#     ls1.insert(ind,val)
#     ls.remove(val)
#
# print(ls1)


#Python List Exercise
#Python program to interchange first and last elements in a list

# ls=[12, 35, 9, 56, 24]
# last=ls[0]
# first=ls[-1]
#
# ls[0]=first
# ls[-1]=last
# print(ls)


#Python Program to Swap Two Elements in a List

# ls=[1,2,3,4,5,6,8,10]
# pos1=1
# pos2=5

# ele1=ls[pos1-1]
# ele2=ls[pos2-1]
#
# for x in ls:
#     if x==ele1:
#         ls[pos1-1]=ele2
#     elif x==ele2:
#         ls[pos2 - 1]=ele1
# print(ls)

# def swap_position(a,b,ls):
#     pos1 = a-1
#     pos2 = b-1
#     ls[pos1],ls[pos2]=ls[pos2],ls[pos1]
#     return ls
# print(swap_position(1,5,ls))

#Swap elements in String list

# ls=['Gfg', 'is', 'best', 'for', 'Geeks']
# strn=""
# for x in ls:
#     for ele in x:
#         if ele=="G":
#             strn=strn+"e"
#         elif ele=="g":
#             strn=strn+"E"
#         elif ele=="E":
#             strn=strn+"g"
#         elif ele=="e":
#             strn=strn+"G"
#         else:
#             strn = strn +ele
#     ls.append(strn)
#     strn=""

# strn=""
# new=[]
# for x in ls:
#     for ele in x:
#Find Maximum of two numbers in Python

# def maximum(a,b):
#     if a>b:
#         return a
#     else:
#         return b
#
# print(maximum(3,6))

#Different ways to clear a list in Python

# ls =[4, 5, 6, 7, 8, 9]
# new=[]
# ls.clear()


# for x in range(len(ls)):
#     ls.pop()
#     print(ls)
# print(ls)
# del ls[:]
# print(ls)

# val=len(ls)-1
# for x in range(len(ls)):
#     new.append(ls[val])
#     val=val-1
#
# print(new)


# ls =[4, 5, 6, 7, 8, 9]
#
#
# n1=0
#
# for x in range(6):
#     ls.insert(n1,ls[-1])
#     ls.pop(-1)
#     n1=n1+1
#
# print(ls)
# ls =[4, 5, 6, 7, 8]
# val=len(ls)//2
# print(val)
# for x in range(6):
#     ls.insert(n1,ls[-1])
#     ls.pop(-1)
#     n1=n1+1
#
# print(ls)

# for x in range(val):
#     ls.append(ls[0])
#     ls.pop(0)
#
# print(ls)


# ls=[15, 6, 7, 10, 12, 20, 10, 28, 10,10,10,5,3,4,6,10]
#
# # val=ls.count(10)
# # print(val)
#
# count=0
# for x in ls:
#     if x==10:
#         count+=1
# print(count)

# ls =[4, 5, 1, 2, 9, 7, 10, 8]
# sum=0
# for x in ls:
#     sum=sum+x
# print(sum)
# val=sum(ls)
# print(float(val)/len(ls))
# ls=[12, 67, 98, 34]
# new=[]
# sum=0
# for x in ls:
#     for ele in str(x):
#         sum=sum+int(ele)
#     new.append(sum)
#     sum=0
# print(new)

# ls=[3, 2, 4]
# n=1
#
# for x in ls:
#     n=n*x
# print(n)



#program to find smallest number in a list

# ls=[20,10,120,1,100,160,23]
# min=ls[0]
# for x in ls:
#     if min>x:
#         min=x
#     else:
#         continue
# print(min)

# max=ls[0]
# for x in ls:
#     if max < x:
#         max=x
# print(max)

# ls=[20,10,120,1,100,160,23]
# ls.sort()
# print(ls[-2])
#program to count Even and Odd numbers in a List
# ls=[2, 7, 5, 64, 14]
# even=0
# odd=0
# for x in ls:
#     if x%2==0:
#         even=even+1
#     else:
#         odd=odd+1
# print(odd,even)


# ls=[12, -7, 5, 64, -14]
# for x in ls:
#     if x >=0:
#         print("Positive num:",x)
#     else:
#         print("Nagative num:", x)

# a=-4
# b=5
#
# for x in range(a,b):
#     if x <0:
#         print("Negative num:",x)

# ls=[12, 15, 3, 10]
# Remove = [12, 3]
# New_List=[]
#
# for x in ls:
#     if x in Remove:
#         pass
#     else:
#         New_List.append(x)
# print(New_List)

#Remove empty tuples from a list

# ls=[(),('ram','15','8'),(),('laxman','sita'),('krishna','akbar','45'),(','),()]
#
# for x in ls:
#     if x ==():
#         ls.remove(x)
#
#
# print(ls)

#Program to print duplicates from a list of integers

# ls=[10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# output_list=[]
# for x in ls:
#     if x  in output_list:
#         pass
#     else:
#         val=ls.count(x)
#         if val>1:
#             output_list.append(x)
# print(output_list)


#Convert List to List of dictionaries

# test_list=["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]
# key_list=['name','id']
# ls=[]
# n=len(test_list)
# for x in range(0,n,2):
#     val={key_list[0]:test_list[x],key_list[1]:test_list[x+1]}
#     ls.append(val)
# print(ls)

#Convert Lists of List to Dictionary

# test_list=[['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
# #{('a', 'b'): (1, 2), ('c', 'd'): (3, 4), ('e', 'f'): (5, 6)}
# dic={}
#
# for x in test_list:
#     key1=x[0]
#     key2=x[1]
#     val1=x[2]
#     val2=x[3]
#     tup_key=(key1,key2)
#     tup_val = (val1, val2)
#     dic[tup_key]=tup_val
# print(dic)

# test_list1 = [ [1, 2], [3, 4], [5, 6] ]
# test_list2 = [ [3, 4], [5, 7], [1, 2] ]
#
# ls=[]
#
# for x in test_list1:
#     if x not in test_list2:
#         ls.append(x)
# for x in test_list2:
#     if x not in test_list1:
#         ls.append(x)
# print(ls)

# ls=[1, 3, 5, 6, 3, 5, 6, 1]
# ls1=[]
# prod=1
# for x in ls:
#     if x in ls1:
#         pass
#     else:
#         ls1.append(x)
#         prod=prod*x
# print(prod)

#Extract elements with Frequency greater than K

# ls=[4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
# k=2
# ls1=[]
# for x in ls:
#     if x in ls1:
#         pass
#     else:
#         val=ls.count(x)
#         if val >k:
#             ls1.append(x)
#
# print(ls1)


#Test if List contains elements in Range

# ls=[4,5,6,7,3,9]
# ls.sort()
# print(ls)
# start=ls[0]
# end=ls[-1]
# range_list=[]
#
# for x in (range(start,end+1)):
#     range_list.append(x)
#
# print(range_list)

#program to check if the list contains three consecutive common numbers in Python

# ls=[1, 1, 1, 64, 23, 64, 22, 22, 22]
#
# for x in range(len(ls)-2):
#     if ls[x]==ls[x+1]==ls[x+2]:
#         print(ls[x])

# ls=[1,1,2,3,4,5,1,2,1]
# new=str(ls)
# for x in new:

#Remove Consecutive K element records

# ls= [(4, 5),(5, 6),(1, 3),(0, 0)]
# for x,y in ls:
#     if x==y:
#         val=ls.index((x,y))
#         ls.pop(val)
# print(ls)


#Extract words starting with K in String List
# ls=['Gfg is good for learning','Gfg is for geeks','I love G4G']
# lst=[]
# for x in ls:
#     for ele in x.split():
#         if "l" in ele:
#             lst.append(ele)
#
# print(lst)

# ls=['G','F','G','I','S','B','E','S','T']
# rep="*"
#
# for x in ls:
#     if x!="G":
#         ind=ls.index(x)
#         ls.pop(ind)
#         ls.insert(ind,rep)
#
# print(ls)

# strn1="ComputerScienceStudentsLoveGfg"
# strn=""
# ls=[]
# for x in strn1:
#     if x==x.upper():
#         ls.append(strn)
#         strn=""
#     else:
#         strn=strn+x
#
# print(ls)

#Dictinoary Data types:
# dic={"Student name":"satish","marks":55,"roll no":15,}
# dic1={}
# print(type(dic1))
# print(dic)

# dic=[('a',5),('b',2),('c',6)]
# print(type(dic))
# x=dict(dic)
# print(dic,"\n", x)

# dic={250:'kitkat', 350:'cadbury', 450:'munch'}

# key=int(input("Enter the key to find the corresponding value:"))
#
# if key in dic:
#     print("the value of {} is:".format(key),dic[key])
# else:
#     print("Entred key is not present in dic")

# print(dic)
# dic[600]="five star"
#
# print(dic)
# dic[250]="kurkure"
# print(dic)
#
# del dic[250]
# print(dic)

#creating a dictionary by entering the name and marks into the dictionary
# students=int(input("Enter no of students inf0:"))
# dic={}
# for x in range(students):
#     name=input("Enter the name of student:")
#     marks=int(input("Enter the marks:"))
#     dic[name]=marks
#
# print(dic)
#
#
#
# print('*'*30)
# print('Name','		','Marks')
# print('*'*30)
#
# for x in dic:
#     print(x,'		',dic[x])

# dic={100:"min", 200:"max", False:""}
# print(all(dic))

# set1=(5,6,1,3,4,2)
# val=sorted(set1)
# print(val,set1)

# dic={100:"min", 200:"max", False:"max"}
# dic2={"sathesh":35,"harika":15,100:"fruit"}
# dic.update(dic2)
# print(dic.keys())
# print(dic.values())
# print(dic.items())
#
# # for x in dic.keys():
# #     print(x)
#
# for ele in dic.items():
#     print(ele)
#get the value from the dictionary for the given key
# dictionary={10:"apple",11:"walnut",4:"orange",5:"banana"}
# key=int(input("Enter the key to find the value:"))

# if key in dictionary:
#     print(dictionary[key])

# if key in dictionary:
#     print(dictionary.get(key))

# for x in dictionary:
#     if x == key:
#         print(dictionary.get(key))

#The following program to get the key from the dictionary for the given value

# dictionary={10:"apple",11:"walnut",4:"orange",5:"banana"}
# value=input("Enter the key to find the value:")
# flag=False
# for x,y in dictionary.items():
#     if y==value:
#         print(x)
#         flag=True
#
# if flag==False:
#     print("Given value is not present")

#This program supports to display all the duplicate values associated with the keys
# dic={100:'Apple', 200:'Apple', 300:'Apple'}
# value="Apple"
# for x,y in dic.items():
#     if y==value:
#         print(x)

# dic={100:'Apple', 200:'Apple', 300:'Apple'}

# # dic.pop(100)
# # print(dic)
# # dic[100]="hi"
# # print(dic)
# # print(dic.popitem())
# # print(dic.clear())
# dic.setdefault(300,"hi")
# print(dic)

# dic1={10:"apple",11:"walnut",4:"orange",5:"banana"}
# dic2=dic1.copy()
# dic2.update({15:"walnut"})
# print(dic1,"\n",dic2)

#Write a program to take a dictionary from the keyboard and print the sum of
# dic={"A":5,"B":15,"c":25,"g":2}
# sum=0
# for x in dic:
#     sum=sum+dic[x]
# print(sum)

# ls=dic.values()
# print(sum(ls))

# word="yyyttttuuuuuu"
# dic={}
# for x in word:
#     dic[x]=dic.get(x,0)+1
# print(dic)

#Write a program to find the number of occurrences of each vowel present in the

# word="the old fox jumped into well"
# vowel="aeiou"
# dic={}
# for x in word:
#     if x in vowel:
#         dic[x]=dic.get(x,0)+1
# print(dic)

#List compression

# dic={x:x*2 for x in range(1,6) if x>0}
# print(dic)

# dictionary1={19:"A",20:"B",21:"C",22:"D"}
# dictionary2={18:"E",23:"F",24:"G",25:"H"}
#
# dic3={**dictionary1,**dictionary2}

# print(dic3)

# set1=(1,2,3,4,5)
# set2=(5,6,7,8)
# set3={*set1,*set2}
# print(set3)

# dictionary={ "cars":("Innova","Honda","Maruthi"),"Mobiles":("Samsung","Nokia","Oppo")}
# print(dictionary["cars"][0])

# dic={'rajnish': 9, 'ravi': 10, 'sanjeev': 15, 'suraj': 32, 'yash': 32}
# key='ravi3'
# print(dic.get(key,"not found"))

# dic={}
#
# x,y,z=5,10,2
# dic[x,y,z]=x+y-z
# x,y,z=5,1,2
# dic[x,y,z]=x-y-z
# x,y,z=5,12,2
# dic[x,y,z]=x-y+z
# print(dic)
# places = {("19.07'53.2", "72.54'51.0"):"Mumbai",("28.33'34.1", "77.06'16.6"):"Delhi"}
# a=[]
# b=[]
# city=[]
# val=0
# for x in places:
#     a.append(x[0])
#     b.append(x[1])
#     city.append(places[x])
#     val=val+1
# print(a,"\n",b,"\n",city)

#Python program to find the sum of all items in a dictionary

# dic={'a': 100,'b':200,'c':300}
# dic_sum={}
#
# for x in dic:
#     dic_sum["sum_all"]=dic_sum.get("sum_all",0)+dic[x]
# print(dic_sum["sum_all"])
#
# print(str(dic.__sizeof__())+"bytes")

#Merging two Dictionaries
# dict1 = {'a': 10, 'b': 8}
# dict2 = {'a': 6, 'c': 4}

# dic3={**dict1,**dict2}
# print(dic3)

# dict1.update(dict2)
# print(dict1)

# for x in dict2:
#     if x in dict1:
#         dict1[x]=dict2.get(x)+dict1.get(x)
#     else:
#         dict1[x]=dict2.get(x)
# print(dict1)

# ar1 = [1, 5, 10, 20, 40, 80]
# ar2 = [6, 7, 20, 80, 100]
# ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
#
# val1=len(ar1)
# val2=len(ar2)
# val3=len(ar3)
# lst=[]
# if val1>val2 and val1>val3:
#     for x in ar1:
#         if x in ar2 and x in ar3:
#             lst.append(x)
# elif val2>val3:
#     for x in ar2:
#         if x in ar1 and x in ar3:
#             lst.append(x)
# else:
#     for x in ar3:
#         if x in ar1 and x in ar2:
#             lst.append(x)
#
# print(lst)

# ls=['john','johnny','jackie','johnny',
#             'john','jackie','jamie','jamie',
#             'john','johnny','jamie','johnny',
#             'john']
#
# dic={}
# for x in ls:
#     dic[x]=dic.get(x,0)+1
# print(dic)
#
# for x,y in dic.items():
#     if y==max(dic.values()):
#         print("Yhe winner of eletion:{}".format(x))


#Key with maximum unique values
#dic={"Gfg" : [5, 7, 7, 7, 7], "is" : [6, 7, 7, 7], "Best" : [9, 9, 6, 5, 5]}
# dic={"Gfg" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]}
# dic1={}
#
#
# for x in dic:
#     val=len(set(dic.get(x)))
#     dic1[x]=val
# for x,y in dic1.items():
#     if y==max(dic1.values()):
#         print(x)

#Find all duplicate characters in string
# word="geeksforgeeeks"
# strn=""
# for x in word:
#     if x in strn:
#         pass
#     else:
#         val=word.count(x)
#         if val >1:
#             print(x)
#             strn=strn+x
# word="geeksforgeeeks"
# strn=""
# exstr=""
# for x in word:
#     if x in strn:
#         exstr=exstr+x
#     else:
#         strn=strn+x
# print(strn,exstr)

# word="geeksforgeeeks"
# dic={}
# for x in word:
#     dic[x]=dic.get(x,0)+1
# for x,y in dic.items():
#     if y>1:
#         print(x)

# Group Similar items to Dictionary Values List
# test_list=[4,6,6,4,2,2,4,8,5,8]
# dic={}
# ls=[]
# for x in test_list:
#     if x in ls:
#         pass
#     else:
#         val=test_list.count(x)
#         ls1=[x]*val
#         dic[x]=ls1
#         ls.append(x)
#         ls1=[]
# print(dic)

# word="geeksforgeeks"
# strn=""
# for x in word:
#     val=word.count(x)
#     if val > 1:
#         pass
#     else:
#         strn=strn+x
# print(strn)
#
# k=int(input("Enter the value:"))
#
# if len(strn)<= k:
#     print(strn[k-1])
# else:
#     print("Less than k non-repeating characters in input")


#Replace String by Kth Dictionary value

# test_list=['Gfg','is','Best']
# subs_dict = {'Gfg':[5, 6, 7],'is':[7, 4, 2]}
# K =0
#
# for x in test_list:
#     if x in subs_dict:
#         ind=test_list.index(x)
#         val=subs_dict.get(x)
#         test_list[ind]=val[0]
# print(test_list)

#Ways to remove a key from dictionary
# dic= {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21}
# del dic['Haritha']
# dic.pop('Mani')
# dic.popitem()
# print(dic)

# Replace words from Dictionary
# test_str='geekforgeeks best for geeks'
# repl_dict={'geeks':'all CS aspirants'}
# new_strn=""
# for x in test_str.split():
#     if x =="geeks":
#         new_strn=new_strn+repl_dict.get('geeks')
#     else:
#         new_strn = new_strn+" "+x
# print(new_strn)

#Remove Dictionary Key Words

# test_str='gfg is best for geeks'
# test_dict={'geeks':1,'best':6}
# strn=""
# for x in test_str.split():
#     if x in test_dict:
#         pass
#     else:
#         strn=strn+" "+x
# print(strn)

#Remove all duplicates words from a given sentence

# word="Python is great and Java is also great"
# strn=""
# for x in word.split():
#     if x in strn:
#         pass
#     else:
#         strn=strn+" "+x
# print(strn)

#Remove duplicate values across Dictionary Values
#
# dic={'Manjeet': [1, 4, 5, 6],'Akash': [1, 8, 9],'Nikhil': [10, 22, 4],'Akshat': [5, 11, 22]}
# ls=[]
#
# for x in dic.values():
#     ls.extend(x)
#
# for x,y in dic.items():
#     new = []
#     for ele in y:
#         val=ls.count(ele)
#         if val > 1:
#             pass
#         else:
#             new.append(ele)
#     dic[x]=new
#
# print(dic)

#Dictionary to find mirror characters in a string
# original='abcdefghijklmnopqrstuvwxyz'
# reverse ='zyxwvutsrqponmlkjihgfedcba'
# k=5
# word="pneumonia"
#
# prefix=word[0:k]
# suffix=word[k:len(word)]
#
# for x in suffix:
#     ind=original.find(x)
#     rev=reverse[ind]
#     prefix=prefix+rev
# print(prefix)

#Counting the frequencies in a list using dictionary in Python
#
# lst=[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
# dic={}
#
# for x in lst:
#     dic[x]=dic.get(x,0)+1
# for x,y in dic.items():
#     print(x,":",y)

#Dictionary Values Mean
# dic= {"Gfg" : 4, "is" : 4, "Best" : 4, "for" : 4, "Geeks" : 4}
# mean=sum(dic.values())//len(dic)
# print(mean)

#set and counter to check if frequencies can become sam
# word='xyyzz'
# dic={}
# for x in word:
#     dic[x]=dic.get(x,0)+1
#
# same = list(set(dic.values()))
# print(same)

#Possible Words using given characters in Python
# lst=["go","bat","me","eat","goal","boy", "run"]
# arr=['e','o','b', 'a','m','g', 'l']
#
# for ele in lst:
#     flag=True
#     for x in ele:
#         if x in arr:
#             flag=True
#         else:
#             flag=False
#     if flag==True:
#         print(ele)

# test_dict = {'gfg' : {'Manjeet' : 5, 'Himani' : 10},
#              'is' : {'Manjeet' : 8, 'Himani' : 9},
#              'best' : {'Manjeet' : 10, 'Himani' : 15}}
# new_dic={}
#
# for x in test_dict:
#     sub_dic=test_dict.get(x)
#     maax_val=max(sub_dic.values())
#     new_dic[x]=maax_val
# max_val1=max(new_dic.values())
# for x,y in new_dic.items():
#     if y==max_val1:
#         print(x)

#Extract values of Particular Key in Nested Values
#
# test_dict = {'Gfg' : {'a':7,'b':9,'c':12},'is': {'a':15,'b':19,'c':20},'best':{'a':5,'b':10,'c':2}}
# ls=[]
# for sub_dic in test_dict.values():
#     val=sub_dic.get('c')
#     ls.append(val)
# print(ls)

#Extract Key’s Value, if Key Present in List and Dictionary

# ls=["Gfg","is","Good","for","Geeks",'Best']
# test_dict={"Gfg":5,"Best":6}
# k="Gfg"
# for x in ls:
#     if x in test_dict:
#         print(test_dict.get(x))

#Remove keys with Values Greater than K ( Including mixed values )
#

# dic={'Gfg':3,'is':7,'best':10,'for':6,'geeks':'CS'}
# ls=[]
# for x in dic:
#     val=dic.get(x)
#     if str(type(val))=="<class 'int'>":
#         if val >= 7:
#             ls.append(x)
#
# print(ls)
#
# for x in ls:
#     dic.pop(x)
# print(dic)

# new={}
# for x in dic:
#     if dic.get(x) in ls:
#         pass
#     else:
#         new[x]=dic.get(x)
# print(new)

# Append Dictionary Keys and Values ( In order ) in dictionary
# dic={'Gfg':1,'is':2,'Best':3}
# # ls=[]
# # for x in dic.keys():
# #     ls.append(x)
# # for y in dic.values():
# #     ls.append(y)
# # print(ls)
# lis=list(dic.keys())+list(dic.values())
# print(lis)

#Keys associated with Values in Dictionary

# test_dict = {'gfg':[1, 2, 3],'is':[1, 4],'best':[4, 2]}
#Output : {1: [‘is’, ‘gfg’], 2: [‘gfg’, ‘best’], 3: [‘gfg’], 4: [‘is’, ‘best’]}
# result_dict={}
#
# for key, val in test_dict.items():
#     for ele in val:
#         if ele in result_dict:
#             result_dict[ele].append(key)
#         else:
#             result_dict[ele] = [key]
# print(result_dict)

# import collections
#
# object_person=collections.namedtuple("object_person","Name Age Marks Gender")
# P1=object_person("Satish",25,55,"M")
# print(P1.Gender)
# print(P1[1])
# print(getattr(P1,"Marks"))

# from collections import OrderedDict
# dic={}
# dic["a"]=1
# dic["b"]=2
# dic["c"]=3
# dic["d"]=4
# dic["e"]=5
# # print(dic)
#
# # od=OrderedDict()
# # od["a"]=1
# # od["b"]=2
# # od["c"]=3
# # od["d"]=4
# # od["e"]=5
# new=OrderedDict(dic)
# print(new)
#
# new["b"]=10
# print(new)


from collections import Counter
# ls=[1,2,3,4,5,1,2,3,4,5,1,2,3,4]
# print(Counter(ls))
# tup=("a","b")
# print(Counter(tup))
# word="Welcome to python"
# print(Counter(word))
# dic={'x': 4, 'y': 2, 'z': 2}
# print(Counter(dic))

# dic=Counter(ls)
# print(dic)
# for x,y in dic.items():
#     print(x,y)

#functions

# def calucalte(a,b):
#     print("The Sum:",a+b)
#     print("The Product:", a * b)
#     if b==0:
#         print("The vlue {} is not disible".format(b))
#
#     else:
#         print("The Divsion:", a / b)
#
# calucalte(5,0)
# calucalte(30,23)
# calucalte(3,2)

# def calling(name):
#     print("Hi good morning",name)
# calling("Satish")

# def suqre_root(num):
#     res=num**2
#     print("The squre root of {} is:".format(num),res)
#
# suqre_root(5)

# def greter_than_1(num):
#     return num>1
# val=greter_than_1(1)
# print(val)

# def sum(a,b):
#     sum1=a+b
#     return
# print(sum(1,2))
# num=4
# fact=1
#
# for x in range(1,num+1):
#     fact=fact*x
# print(fact)

# def factorial(num):
#     fact=1
#     while num>=1:
#         fact = fact * num
#         num=num-1
#     return fact
# print(factorial(3))

# def sum_sub(a,b):
#     sum=a+b
#     sub=a-b
#     return sum,sub
#
# print(sum_sub(5,6))

# def calc(a,b):
#     sum=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return sum,sub,mul,div
#
# obj=calc(3,2)
# print(obj[1])
# print(type(obj))
# print(obj)
# for x in obj:
#     print(x)

# def calucalte(a,b):
#     print("The Sum:",a+b)
#     print("The Product:", a * b)
#     if b==0:
#         print("The vlue {} is not disible".format(b))
#
#     else:
#         print("The Divsion:", a / b)
#
# # calucalte(5,6)
# calucalte(5,b=6)

# def wish(name,msg="Good morning"):
#     print("Hi",name,msg)
#
# wish("Harika")

# def outter():
#     print("outer function started")
#     def inner():
#         print("Innner function executed")
#     inner()
#     print("outer function completed")
#
# outter()

# def outter():
#     def inner():
#         print("Innner function executed")
#
#     return inner()
#
# outter()

# def fun1(fun):
#     fun()
#
# def fun2():
#     print("Hi good morn")
# fun1(fun2)

# def decor_add(fun):
#     def inner(a,b):
#         if b==0:
#             print("Division by zero not possible")
#         else:
#             fun(a,b)
#     return inner
#
#
#
# def div(a,b):
#     val=a/b
#     print(val)
#
# with_decor=decor_add(div)
# with_decor(5,0)


# def decor(func):
#     def inner(name):
#         if name=="Tarun":
#             print("#"*30)
#             print("Hello Tarun, you are very important for us..!!")
#             print("Very Very Good Morning..!!")
#             print("#"*30)
#         else:
#             func(name)
#     return inner
# def wish(name):
#     print("Good Morning:",name)
# decorated_wish=decor(wish)
# decorated_wish("Tarun")

# def decor_for_add(func):
#     def inner(a,b):
#         print("#"*30)
#         print("TheSum:",end="")
#         func(a,b)
#         print("#"*30)
#     return inner
#
# @decor_for_add
# def add(a,b):
#     print(a+b)
#
# add(20,0)

# def outer(a,b):
#     def inner():
#         val=a+b
#         return val
#     return inner()
#
# def outer1(a,b):
#     def inner(a,b):
#         val=a+b
#         return val
#     return inner(a,b)
#
# su1=outer(5,6)
# su2=outer1(5,3)
# print(su1,su2)

# def fun(*numbers):
#     tot=0
#     for x in numbers:
#         tot=tot+x
#     return print(tot)
#
# fun(1,2,3,1)


# def fun(*x,**y):
#     print(x,y)
#
# fun(10,15,name="satish",marks=15)

# def function(arg1, arg2, arg3=5, arg4=15):
#     print(arg1, arg2, arg3, arg4)
#
#
# function(3, 2) #32515
# function(10, 20, 30, 40)#10 20 30 40
# function(25, 50, arg4=100)#25 50 5 100
# function(arg4=3, arg2=1, arg2=5) #1 5 5 3

# c=15
# def fun():
#     global c
#     c = 23
#     print(c)
#
# def fun1():
#     print(c)
#
# fun()
# fun1()

# c=15
# def fun():
#     c = 23
#     print(globals().get('c'))
#     print(c)
#
#
# fun()


# def fatorail(n):
#     if n ==0:
#         result=1
#     else:
#         result=n*fatorail(n-1)
#     return result
# for x in range(6):
#     print("the factrail value of {} is :".format(x),fatorail(x))



































