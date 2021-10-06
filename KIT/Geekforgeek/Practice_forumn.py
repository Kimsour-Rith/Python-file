# import time
# inp = float(input("Input time to sleep:"))
# res = inp/1000
# time.sleep(res)
# print(res," millisecond has pass")
# def factorial(n):
#     if n ==1 or n==0:
#         return 1
#     return n*factorial(n-1)
#
# def permutation(n,r):
#     return factorial(n)//factorial(n-r)
#
# def combination(n,r):
#     return factorial(n)//factorial(n-r)//factorial(r)
#
# print(" The permutation of 5 is: ",permutation(5,2))
# print(" The combination of 5 is: ",combination(5,2))

import time
# def time(arr,delay):
#
#
# def quick_sort(arr):
#     if len(arr)<=1:
#         return arr
#     else:
#         pivot=arr.pop()
#
#     item_greater=[]
#     item_lower=[]
#     for item in arr:
#         if item < pivot:
#             item_lower.append(item)
#         else:
#             item_greater.append(item)
#
#     return quick_sort(item_lower)+[pivot]+quick_sort(item_greater)      # it will repeat sorting the element and go over and over just like loop function
#
#
# print(quick_sort([15,60,9,51,75,12,36,85,90]))



# inp1 = input("Input a string:")
# inp2 = input("Input a file name:")
# f = open(inp2,"r")
# read = f.readlines()
# for i in read:
#     if inp1 in i:
#         print(inp1)


# set1 ={1,2,3,4,5,6,7,8,9,10}
# set2 = {1,2,6,7,23,14,26}
# res = set1.union(set2)
# list_re = list(res)
# print(list_re)

#write a function to solve a quadratic equation
#the parameters are the coefficient of the equation

#import math
# a = int(input("Input a:"))
# b = int(input("Input b:"))
# c = int(input("Input c:"))
# d = (b**2) - (4*a*c)
# x1 = ((-b - math.sqrt(d))/ (2*a))
# x2 = ((-b + math.sqrt(d))/ (2*a))
# print(x1,x2)

# import math
# def quadratic_euation(a,b,c):
#     d = (b ** 2) - (4 * a * c)
#     x1 = ((-b - math.sqrt(d)) / (2 * a))
#     x2 = ((-b + math.sqrt(d)) / (2 * a))
#     return x1,x2
#
#
# print("The roots are: ",quadratic_euation(1,5,6))