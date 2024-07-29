import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))

#ASC11 ord() and Char

# print(ord("A"))
# print(ord("a"))
# print(chr(65))
# print(chr(97))
#
#
# a="Apple"
# b="APple"
# print(a>b)
# print(10<20<10<50)
# a=[10]
# b=[10]
# print(a == b)
# print(a is b)
# print(id(a),id(b))


# a=199
# print(type(a))
#
# b=0b111
# print(b)
#
# c=0O7643 #0o small o as well
# print(c)
#
# d=0X123abc
#
# print(d)

# integers,base 10: 0 to 9
# binary,base 2: 0 or 1 ==> 0b1101
# octognonal,base 8:1 to 7 ==> 0o or 0O ==>0o12345
# hexadeimal,base 16:1 to 9 and a to f or (A to F) ==>0x1239abc

# #x=10+5j
# x=0x123ab+5j
# print(x)
# print(x.real)
# print(x.imag)
# #id(),chr(),type(),ord(),real,imag
#
# print(int(True))

# x=5
# x+=5 #(x=x+5,x=x-5,x=x/5,x=x%5,x=x//5,x=x**5)
# print(x)

# x=5
# x%=5
# print(x)
#
# a=12
# b=12
# c=10
# result_min=a if a<b and a<c else b if b<c else c
# result_max=a if a>b and a>c else b if b>c else c
# print(result_min)
# print(result_max)
#
# resilt_big="Equal" if a==b else "bigger" if a>b else "smaller"
# print(resilt_big)


# stn='abcdefghij'
# stn[1:6:2] bcdef bdf
#
# string[1:6:2] => bcdef bdf
# string[::1] =>abcdefghij
# string[::-1] =>abcdefghij==>jihgfedcba
# string[3:7:-1] =>defg ==>gfed
# string[7:4:-1] =>emty
# string[0:10000:1] =>abcdefghij
# string[-4:1:-1]=>g
# string[-4:1:-2] =>
# string[5:0:1] =>
# string[9:0:0] =>
# string[0:-10:-1]=>
# string[0:-11:-1] =>
# string[0:0:1] =>
# string[0:-9:-2] =>
# string[-5:-9:-2] =>
# string[10:-1:-1] =>
# string[10000:2:-1] =>


# strn1="satheesh"
# strn2="harika"
#
# if strn1==strn2:
#     print("both strings are equal")
# elif strn1>strn2:
#     print("strn1 is grater")
# else:
#     print("strn2 is grater")
#
# print(ord('s'))
# print(chr(115))

# strn=" satheesh "
# print(strn.rstrip())
# print(strn.lstrip())
# print(strn.strip())

# strn=" satheesh"
#
# print(strn.find("th"))
# print(strn.find("h"))
# print(strn.rfind("h"))
# print(strn.find("z"))
# print(strn.find("h",1,5))
# print(strn.index("e"))
# print(strn.rindex("e"))
# try:
#     val=strn.index("e")
#     print(val)
#     print("the is sub string")
# except ValueError:
#     print("it is not sub string")

# strn="ABCABCABCA"
# sub="ABC"
# val=strn.find(sub)
# if val==-1:
#     print("it is not apart of string")
# while val !=-1:
#     print("ABC is at present at postion {}".format(val))
#     val=strn.find(sub,val+len(sub),len(strn))
# print(strn.count(sub,0,6))

# strn="satheesh"
# print(strn.replace("e","aaa"))
#
# strn="cher cher tech"
# print(strn.replace(" ",""))
# print(strn.count(" "))
# strn="The Wooden floor had cracked and split in the heat"
# lst=strn.split()
# date1="12-27-47-16-900"
# l2=date1.split("-")
# print(lst,l2)
#
# txt= "apple#banana#cherry#orange"
# print(txt.split("#",2))

# lst=["1","2","hello"]
# new="#".join(lst)
# print(new)
# dat=['04', '05', '2019']
# new_date="-".join(dat)
# print(new_date)

# strn="The Wooden floor had cracked and split in the heat"
# print(strn.upper())
# print(strn.lower())
# print(strn.swapcase())
# print(strn.title())
# print(strn.capitalize())

# strn="satheesh"
# new=strn[0].upper()+strn[1:len(strn)-1]+strn[-1].upper()
# print()
# print(new)
# print(strn.startswith("sa"))
# print(strn.endswith("she"))
#
# isalnum()
# isalpha

# ls=[5,10,4,"hi",10,10,"satheesh"]
# print(type(ls))
#
# print(ls)
#
# ls.append(5)
# print(ls)
# ls.append("harika")
# print(ls)
#
# ls.remove("satheesh")
# print(ls)
# ls.remove(10)
# print(ls)
# ls[1]="joshvik"
# print(ls)

# ls=eval(input("enter the list"))
# print(ls)
# print(type(ls))

# ls=list("apple")
# print(ls)

# ls=list(range(7))
# print(ls)

# str="hi how are you satheesh"
# ls=str.split()
# print(ls)

# ls=[5,10,4,"hi",10,10,"satheesh"]
# print(ls[2])
# print(ls)
# print(ls[::-1])
# print(ls)
# integer=0
# while integer < len(ls):
#     print(ls[integer])
#     integer+=1
# ls=[0,1,2,3,4,5,6,7,8,9,10]
# lst=ls*3
# print(lst)
# for x in ls:
#     if x%2 != 0:
#         print(x)
# print(len(ls))
# integer=0
# for x in ls :
#     print("positive {} and nagative {} is".format(integer,integer-len(ls)),ls[integer])
#     integer=integer+1

# def list(num):
#     for x in num:
#         print(x)
# list(ls)

# ls=[[10,20,30],[40,50,60],[70,80,90]]
# for x in ls:
#     for i in x:
#         print(i,end=' ')
#     print()


# for x in range(7):
#     lst.append(x)
# print(lst)
# lst=[x**2 for x in range(10) if x%2==0]
# print(lst)

# ls=['Apple','Banana','Carrot','Dragon fruit']
# new=[x[0] for x in ls]
# print(new)

# st="the quick brown fox jumps over the lazy dog"
# ls=st.split()
# print(ls)
# new=[[word.upper(),len(word)] for word in ls]
# print(new)

# vowels=['a','e','i','o','u']
# word=input("Enter the search for volwes :")
# lst=[]
# for x in word:
#     if x in vowels:
#         lst.append(x)
#
# print(lst)

# lis=['H','e','l','l','o']
# lis.append("hi")
# print(lis)
# lis.append((1,2))
# print(lis)
# ls=[1,2,3]
# lis.extend(ls)
# print(lis)
# lis.pop()
# print(lis)
# lis.pop(-2)
# print(lis)
# lis.insert(0,25)
# print(lis)
# lis.count('l')
# print(lis)
# lis.sort()
# print(lis)
# lis.reverse()
# print(lis)


#tuple
# tup=(1,2,1,"hi")
# print(tup[0])
# print(tup[-1])
# tup[0]=10
# print(tup)

# tup=1,2,3,5,"hi"
# tup1=()
# print(tup)
# print(type(tup))
# print(type(tup1))
# tup=()
# tup=tuple("satish")
# tup=eval(input("enter tiple:"))
# tup=tuple(range(8))
# str="satish how are you"
# tup=tuple(str.split())
# print(tup)
# tup=(10,20,30,10,40,50)
# print(tup.count(10))
# print(tup.index(10,1,5))

# new=sorted(tup)
# new1=reversed(tup)
# print(tuple(new))
# print(tuple(new1))

# tup=(10,20,30,10,40,50)
# print(max(tup))

#packing and unpacking the tuple
# a=10
# b=5
# c=15
# d=12
# tup=(a,b,c,d)
# print(tup)

# tup1=(1,2,3,4,5)
# a,b,c,d,e=tup1
# print(a,b,c)
# ls=[4,4,5,67,7,7,8,2]
# s={1,2,3,4,5,6}
# s1=eval(input("inter set"))
# print(s)
# print(set(ls))
# print(s1)
# print(set(range(7)))
# print(set("range(7)"))

# set1={11,23,45}
#
# set3=set1*2
# print(set3)

# s={1,2,3,4,5}
# s.add(6)
# print(s)
# s.update(range(7,12),"hello")
# print(s)
# #s.remove(5)
# s.discard(25)
# # s.pop()
# print(s)
# s.add(2)
# s.update("helloe",[1,2,3,4],range(5))
# s.remove(5) #erro if not
# s.discard(5) #no error
# s.pop() #random deletion
# s.clear()
# s.copy()
# s1.union(s2)
# s1.intersection(s2)


# set1={5,10,15,24}
# set2={6,12,18,24}
# set3=set1.union(set2)
# set4=set1.intersection(set2)
# print(set3,set4)

# selection
# if
# if else
# if elif
# if elif else

# name=input("Enter the name:")
# if name.lower()=="satheesh":
#     print("Hello {} how are you".format(name))
# else:
#     print("How are you")

# brach=input("Enter the brach name:")
# if brach.lower()=="ec":
#     print("it is software brach")
# elif brach.lower()=="mech":
#     print("it is mechanical brach")
# elif brach.lower()=="csc":
#     print("it is software brach")
# else:
#     print("ther branches are not recommended")


# a=int(input("Enter a number"))
# b=int(input("Enter a number"))
# c=int(input("Enter a number"))
# if a>b and a>c:
#     print("{} is bigger number".format(a))
# elif b>c:
#     print("{} is bigger number".format(b))
# else:
#     print("{} is bigger number".format(c))
# val=a if a>b and a>c else b if b>c else c
# print(val)

# num=int(input("Enter a number"))
#
# if num>=1 and num<=100:
#     print("{} is in b/w 100".format(num))
# else:
#     print("{} is NOT in b/w 100".format(num))

# s="banana"
# i=0
# for x in s:
#     print("the index at {} is : {}".format(i,s[i]))
#     i+=1


# for x in range(0,21):
#     if x%2==0:
#         print(x)
# sum=0
# for x in range(10,0,-1):
#     sum=sum+x
# print(sum)

# print(sum([1,2,3,4,5]))

#
# n=5
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i=i+1
# print(sum)
# n=6
# sum=0
# for x in range(1,n+1):
#     sum=sum+x
# print(sum)

# for x in range(5):
#     if x==3:
#         print("element found stop")
#         break
#     else:
#         print("Element not found")

# for x in range(10):
#     if x%2==0:
#         continue
#     else:
#         print(x)

# ls=[10,20,500,700,50,60]
# for ele in ls:
#     if ele >= 500:
#         print("order is not proccesd {}".format(ele))
#         continue

# ls =[10,20,0,5,0,30]
#
# for x in ls:
#     if x == 0:
#         #print("zero cant dived")
#         continue
#     print("100//{} vale is :{}".format(x,100//x))

# for letter in 'chercher.tech':
#    if letter == 't':
#       pass
#       print('This is pass block')
#    print ('Current Letter :', letter)
#
# print ("Good bye!")

# for x in range(10):
#     if x ==5:
#         pass
#     print(x)

# s1=10
# s2=s1
# s3=s2
# print(id(s1),id(s2),id(s3))
# del s1
# print(id(s2),id(s3))

#prime numbers


# n=int(input("Enater a integer number:"))
# is_prime=True
# if n<=1:
#     print("It is not a prime number")
#
# else:
#     for i in range(2,n):
#         if n%i==0:
#             is_prime = False
#             break
# if is_prime == True:
#     print("{} is a prime number".format(n))
# else:
#     print("{} is not a prime number".format(n))

# n=int(input("Enter a number:"))
# n1=2
# while n1<=n:
#     is_prime=True
#     for i in range(2,n1):
#         if n1%i==0:
#             is_prime=False
#             break
#     if is_prime==True:
#         print(n1)
#     n1=n1+1


#string practice:




