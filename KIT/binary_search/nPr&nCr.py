def factorial(n):
    if n ==1 or n==0:
        return 1
    return n*factorial(n-1)

def permutation(n,r):
    return factorial(n)//factorial(n-r)

def combination(n,r):
    return factorial(n)//factorial(n-r)//factorial(r)

print(" The permutation of 5 is: ",permutation(5,2))
print(" The combination of 5 is: ",combination(5,2))

#Write a program to print the sum of the following series 1 + 1/2 + 1/3 +. …. + 1/n
# def sumseries(n):
#     sum =0
#     for j in range(1,n+1):
#         sum += 1/j
#     return sum
# print(sumseries(3))

# 14. Write a Python function to check whether a string is a pangram or not.
#  Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# def pangram(string):
#     st = string.lower()
#     lists = []
#     for i in st:
#         if i.isalpha():
#             lists.append(i)
#     new_set = set(lists)
#     if len(new_set) == 26:
#        ans = 'is pangram'
#     else:
#         ans = 'is not pangram'
#     return ans


#print(pangram("The quick brown fox jumps over the lazy dog"))

#
# def bubble_sort(list):
#     for i in range(len(list)-1,0,-1):
#         print(i)
#         for j in range(i):
#             print(j)
#             if list[j]>list[j+1]:
#                 temp = list[j]
#                 list[j] = list[j+1]
#                 list[j+1] = temp
#             print(list)
#         print('hor-'*10)
#
# list = [50,65,8,12,65,7]
# bubble_sort(list)
# print(list)
#
# # insertion_sort
# def insertion_sort(list):
#     for i in range(len(list)):


# def sellection_sort(arr):
#     ls =[]
#     i=0
#     while len(ls) < len(arr):
#         minimum = min(arr)
#         #arr[minimum], arr[i] = arr[i], arr[minimum]
#         ls.append(min(arr))
#         i += 1
#         print(minimum)
#     return ls
# arr = [50,65,8,12,65,7]
# sellection_sort(arr)
# print(arr)


# def selectionSort(num):
#     for i in range(len(num)):
#         min_idx = i
#         for j in range(i+1, len(num)):
#             if num[min_idx] > num[j]:
#                 min_idx = j
#         num[i], num[min_idx] = num[min_idx], num[i]
#         print(num)
#     return num
#
#
# print(selectionSort([1,87,78,34,20,100,5,22,7,90,12]))



# gussing game
# import random
# name= input("Please input your name before start the game: ")
# answer= input(f'Hey {name} are you ready to take the challenge? Press y/Y to start any other key to stop: ')
#
# while True:
#     rannum = random.randint(1, 10000)
#     print(rannum)
#     if answer == 'y' or answer == 'Y':
#         print("I have number in mind (1,10000) you have maximum 6 attempts to guess the number")
#
#         for i in range (1,7):
#             if i<6:
#                 inp = int(input(f'Attempt {i}:'))
#                 if inp == rannum:
#                     print(f'Brilliant! {name}, you have guessed it in{i} attempts')
#                     answer= input('Press y/Y to start any other key to stop:')
#                     if answer == 'y' or 'Y':
#                         break
#                     else :
#                         exit()
#                 elif inp > rannum:
#                     print(f'Attempt{i} failed,guess a number lesser than that')
#                 elif inp < rannum:
#                     print(f'Attempt{i} failed,guess a number higher than that')
#             else:
#                 inp_final = int(input(f'Your last chance Attempt 6:'))
#                 if inp_final == rannum:
#                     print(f'Brilliant!{name}, you have guessed it in 6 attempts')
#                     answer = input("press y/y if you want to restart the game n/N to quit:")
#                     if answer == 'y' or answer == 'Y':
#                         pass
#                     else:
#                         break
#                 else:
#                     print(f'Attempt 6 failed, You have lost all your chances Better luck next time')
#                     answer = input("press y/y if you want to restart the game n/N to quit:")
#                     if answer == 'y' or answer == 'Y':
#                         pass
#                     else:
#                         break
#         else:
#             break

# Bootcamp  20 ascii value
# while True:
#     print("Press 1 to decode:")
#     print("Press 2 to encode:")
#     answer = int(input(""))
#     if answer == 1:
#         inp = input("Enter the string to encode:\n")
#         a = ""
#         for i in inp.upper():
#             if ord(i) in range(65,78):
#                 new_alp = ord(i) + 13
#                 decode = chr(new_alp)
#                 a += decode
#             elif ord(i) in range(78,91):
#                 new_alp = ord(i) - 13
#                 encode = chr(new_alp)
#                 a += encode
#         print("The decode text is",a)
#     elif answer == 2:
#         inp = input("Enter the string to decode:\n")
#         b = ""
#         for i in inp.upper():
#             if ord(i) in range(65,78):
#                 new_alp = ord(i) + 13
#                 decode = chr(new_alp)
#                 b += decode
#             elif ord(i) in range(78,91):
#                 new_alp = ord(i) - 13
#                 encode = chr(new_alp)
#                 b += encode
#         print("The encode text is",b)
#
#     op = input("Do you want to continue? [Y/N]\n")
#     if op == 'y' or op == 'Y':
#         continue
#     elif op == 'n' or op == 'N':
#         break
#
#     else:
#         print("Invalid input")
#         break
#
# merge sort
# def merge_sort(arr):
#     if len(arr) == 1:
#         return arr
#     mid = len(arr)//2
#     left_arr = merge_sort(arr[:mid])
#     right_arr = merge_sort(arr[mid:])
#     return merge(left_arr,right_arr)
# def merge(list1,list2):
#     i = 0
#     j = 0
#     merge_list = []
#     while i < len(list1) and j < len(list2):    # example: list1 = [1,3] list2=[3,4]
#         if list1[i] <= list2[j]:
#             merge_list.append(list1[i])
#             i += 1
#         else:
#             merge_list.append(list2[j])
#             j += 1
#     merge_list.extend(list1[i:])
#     merge_list.extend(list2[j:])
#     return merge_list
#
# lists = [11,33,4,2,21,76,15,90,0]
# print(merge_sort(lists))
# try:
#     f = open("E:/KIT/Homework/asd","r+")
#     read = f.read()
#     print(read)
# except Exception as e:
#     print(e)

# try:
#     f= open("E:/KIT/Homework/asd","r+")
#     write= f.write("Good evening")
#     print(write)
#     print("File write successfully")
# except Exception as e:
#     print(e)
# finally:
#     f.close()
#     print("File close successfully")

# try:
#     f= open("E:/KIT/Homework/asd","w+")
#     f.write("Good evening")
#     f.seek(0)
#     read = f.read()
#     print("File write successfully")
# except Exception as e:
#     print(e)
# finally:
#     f.close()
#     print("File close successfully")

try:
    f= open("E:/KIT/Homework/asd","a+")
    read1= f.read()
    print(read1)
    f.write(" I am a girl")
    f.seek(0)
    read = f.read()
    print(read)
    print("File write successfully")
except Exception as e:
    print(e)
finally:
    f.close()
    print("File close successfully")