# practising how to implement linkedlist in python 
# class Node:
#     def __inti__(self):
#         self.data=self.data
#         self.next=None

# class Linkedlist:
#     def __init__(self):
#         self.head=None

#     def printlist(self):
#         if self.head is None:
#             print("list is empty")
#         else:
#             n=self.head
#             while n is not None:
#                 print(n.data)
#                 n=n.next

# l1=Linkedlist()
# l1.printlist()

# sum=0
# for i in range(1,11):
#     sum=sum+i
# print(sum)

# a=[1,2,3,4]*2
# for i in range(len(a)):
#     a[i]=a[i]*3
# print(a)

# on array we can directly perform mathematical operations without using loop
#but in list we have to use loop to perform mathematical operations on each element of list
import numpy as np
# b=[1,2,3,4]*3
# a=np.array(b)
# new=a*2
# print(new)

# a=[1,2,3,4] 
# a=np.array(a)
# print(a.ndim)

# b=np.array(34)   # it is a scalar
# print(b.ndim)


# np.linspace(1,10,5)  # it will generate 5 numbers between 1 and 10 with equal distance
# print(np.linspace(1,10,5))

import time

#logarithmic space array
# np.logspace(1,10,5)  # it will generate 5 numbers between 10^1 and 10^10 with equal distance
# print(np.logspace(1,10,5))          # (starting power value of 10, ending power value of 10, number of values to generate)
# print(np.zeros(5))  # it will generate an array of zeros
# print(np.zeros([2,3]))  # it will generate an array of zeros with 2 rows and 3 columns
# print(np.ones(2))       # it will generate an array of ones
# print(np.ones([2,3],dtype=int))
# start=time.time()
# print(np.full([2,4],7))  # it will generate an array of sevens with 2 rows and 4 columns where 7 will be the default value
# print(time.time()-start)
# print(np.empty)        # it will create an array without initializing the values, it will contain random values
# print(np.empty([2,3],dtype=int))        # it will create an array without initializing the values, it will contain random values
# print(np.arange(1,10,1))                # it will generate an array of numbers from 1 to 10 with a step of 1

# list=[1,2,3,4,5,6]
# print(list[-1:-(len(list)+1):-1])                          # it will print the last two elements of the list
# print(list[: :2])                         # it will print every second element of the list starting from the first element
# print(list[-1::])
arr=np.array([1,2,3,4,5,6,7,8,9])
arr=arr.reshape(3,3)
# print(arr)
# # print(arr[0:,0:3])
# print(arr[2:,1:3])    # syntax: array[row_start:row_end, column_start:column_end]   
# for x in np.nditer(arr):    # it will return the value of each element in the array
#     print(x)

# for ind,x in np.ndenumerate(arr):        # it will return the index and the value of each element in the array
#     print(ind,x)             


# copy = arr[:3].copy()        # it will create a copy of the array
# print(copy)    
# copy[0:1,0:1]=100
# print(copy)

# print(copy.transpose())                # it will transpose the array


# str="kanchan"
# print(str[:2])
# print(str[:2:2])

#sets in python
# sets are unordered collection of unique elements ,and they are mutable
# frozenset is an immutable version of set, unordered collection of unique elements
a={11,2,2,3,4,5,6,7,8,9}
# print(a)
# print(type(a))
# print(frozenset(a))
# to access the elements of set we can use for loop
# for i in a:
#     if i%2==0:
#         continue
#     print(i)

# set methods
# a.add(10)      # it will add the element 10 to the set
# print(a)
# a.remove(2)    # it will remove the element 2 from the set
# print(a)
# a.discard(2)   # it will remove the element 2 from the set if it is present, if it is not present then it will do nothing
# print(a)
# a.pop()        # it will remove and return a random element from the set
# print(a)
# a.clear()      # it will remove all the elements from the set
# print(a)
# dictionary in python
# dictionary is a collection of key-value pairs, and it is mutable

# str="K,A,N,C,H,A,N"
# # s=str.split(",")
# # print(s)
# # AF="-".join(s)
# # print(AF)

# print("K" in str)   # it will return True if K is present in the string, otherwise it will return False
# print(str.endswith("N"))   # it will return True if the string ends with N, otherwise it will return False
# print(str.startswith("K"))   # it will return True if the string starts with K, otherwise it will return False
# print(str.count("A"))   # it will return the number of times A is present in the string
# print(str.find("C"))    # it will return the index of the first occurrence of C
# print(str.find("Z"))    # it will return -1 if Z is not present in the string
# print(str.index("C"))   # it will return the index of the first occurrence of C
# print(str.isdigit())    # it will return True if all the characters in the string are digits, otherwise it will return False
# print(str.isalpha())    # it will return True if all the characters in the string are alphabets, otherwise it will return False
# print(str.isalnum())    # it will return True if all the characters in the string are alphanumeric, otherwise it will return False
# print(str.islower())    # it will return True if all the characters in the string are lowercase, otherwise it will return False
# print(str.isupper())    # it will return True if all the characters in the string are uppercase, otherwise it will return False


# a=[1,2,3,4,5]
# b=[3,7,8,9,10]
# c=a+b
# print(c)
# a.extend(b)  # it will extend the list a by adding the elements of list b to it
# print(a)
# a=set(a)  # it will convert the list a into a set
# b=set(b)  # it will convert the list b into a set)
# c=a.intersection(b)  # it will return the common elements between list a and list b
# print(list(c))

# a=[1,2,3,4,5,1]
# for i in a:
#     if a.count(i)>1:
#         print(i,"is duplicATE")
#         break

# question: how to find the duplicate element in a list without using loop
# check if vowels in string
# fibonacci series
# reverse a string
# find the largest and smallest element in a list
# find the second largest and second smallest element in a list
# list comprehension
# lambda function
# map function
# filter function
# reduce function
# dictionary comprehension
# set comprehension
# exception handling
# file handling



# 1.how to find the duplicate element in a list without using loop
# a=[1,2,3,4,5,1]
# if len(a)!=len(set(a)):
#     print("Duplicate Found")

# 2.check if vowels in string
# str="kanchan"
# count=0
# for i in str:
#     if i in "aeiouAEIOU":
#         count+=1
# print(count)

# 3.fibonacci series
# n=int(input("Enter the number of terms in Fibonacci series "))
# a=0
# for i in range(n+1):
#     a=a+i
# print(a)

# 4.reverse a number
# logic
"""
n=667788
rev=0
a=n//10 # removes the last digit
b=n%10  # gives the last digit
rev=rev*10+b  # adds the last digit to the reverse number
n=a  # removes the last digit from the original number
"""
# n=int(input("Enter the number "))
# rev=0
# while True:
#     a=n%10
#     c=n//10
#     rev=rev*10+a
#     n=c
#     if n==0:
#         print(rev)
#         break

# 5.find the largest and smallest element in a list
# a=[1,2,3,4,5]
# print("Largest element:", max(a))
# print("Smallest element:", min(a))


# 6.find the second largest and second smallest element in a list
# a=[1,5,8,3,4]
# a.sort()
# print("Second largest element:", a[-2])
# print("Second smallest element:", a[1])

# 7.list comprehension
# a=[x for x in range(1,11)]
# print(a)
# b=[x for x in range(1,11) if x%2==0]
# print(b)

# 8.lambda function
# add=lambda a,b:a+b
# print(add(5,3))

# 9.duplicate 
# a=[1,2,3,4,5,1]
# duplicate=[]
# for i in a:
#     if a.count(i)>1 and i not in duplicate:
#         duplicate.append(i)
#         a.remove(i)
# print(duplicate)
# print(a)

# 10.map function
# a=[1,2,3,4,5]*2
# result=map(lambda x: x*2, a)
# print(list(result))

# 11.filter function
# a=[2,1,8,3,4,5]
# result=filter(lambda x:x%2==0,a)
# print(list(result))

# 12.reduce function
# from functools import reduce
# a=[1,2,3,4,5]
# result=reduce(lambda x,y:x+y,a)
# res=reduce(lambda x,y:x*y,a)
# print(result)
# print(res)

# decorators in python
# def decorator(func):
#     def initialize():
#         print("Initialize transaction")
#         func()
#         print("transaction completed")
#     return initialize

# @decorator
# def transaction():
#     print("transaction in progress")

# transaction()

# generTORS IN PYTHON
# def generator():
#     for i in range(5):
#         yield i                       # yield is used to return a value from the generator function and it will pause the execution of the function until the next value is requested

# g=generator()
# print(next(g))   # it will return the next value generated by the generator function
# print(next(g))   # it will return the next value generated by the generator function
# print(next(g))   # it will return the next value generated by the generator function
# for i in g:
#     print(i)

# num=5655
# rev=0
# stack=[]
# while True:
#     if len(stack)==0:
#         break
#     else:
#         stack.append(num%10)
#         num=num//10
# print(stack)
# while True:
#     if len(stack)==0:
#         break
#     else: 
#         rev=rev*10+stack.pop()
# print(rev)


# two sum problem
list=[1,2,3,4,5]
# target=5
# for i in list:
#     for j in list:
#         if i+j==target:
#             print(i,j)

# def reverse_number(num):
#     rev=0
#     while True:
#         a=num%10
#         c=num//10
#         rev=rev*10+a
#         num=c
#         if num==0:
#             return rev
# def reverse_string(str):
#     return str[::-1]
# def rev_str(str):
#     rev=""
#     while True:
#         if len(str)==0:
#             return rev
#         else:
#             rev=rev+str[-1]
#             str=str[:-1]
        
# print(reverse_number(667788))
# print(reverse_string("kanchan"))
# print(rev_str("kanchan"))

# l1=[1,2,3]
# l2=[4,5,6]
# result=[]
# for i in range(len(l1)):
#     for j in range(i+1,len(l2)):
#         sum=l1[i]+l2[j]
#         result.append(sum)
# print(result)
# print(result[::-1])


#fibonacci series
# 0 1 1 2 3 5 8 13 21 34
# a=0
# b=1
# print(a,b,end=" ")
# for i in range(10):
#     sum=a+b
#     print(sum,end=" ")
#     a,b=b,sum

# factorial of a number
# n=10
# sum=1
# for i in range(1,6):
#     sum=sum*i
# print(sum)

# list=[1,2,3,4,5]
# for ind,value in enumerate(list):     # enumerate is used to get the index and the value of each element in the list
#     print(ind,value)

# list1=[1,2,3,4,5]
# list2=[6,7,8,9,10]
# for i,j in zip(list1,list2):   # zip is used to iterate over two or more lists simultaneously
#     print(i+j)

for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()         # it will print a pattern of stars and it will print a new line after each row of stars

for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()         # it will print a pattern of stars in reverse order and it will print a new line after each row of stars

for i in range(1,6):
    print(" "*(5-i),end="")
    print("* "*i)

for j in range(5,0,-1):
    print(" "*(5-j),end="")
    print("* "*j)













    
    
