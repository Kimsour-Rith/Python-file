# def sumofcollection(list_num):
#     return sum(list_num)
# result = sumofcollection([50,60,100,85,65])



# def ret_collection_from_fn(ran):
#     list = []
#     for i in ran:
#         list.append(i)
#     return list
# print(ret_collection_from_fn('seanghor'))
# print(ret_collection_from_fn(54))         # Error


# def fetchrecords():
#     listOfUsers = {123:"Kimhour", 134: "Sereyvann", 145: "Ratanak"}
#     return listOfUsers
#
# print(fetchrecords())



# # witout global
# name = 'Momo'
#
# def grading():
#     name = 'Kimsour'
#     grade = 'A'
#     age = 25
#
#
#     print(name)
#     print(grade)
#     print(age)
# grading()
#
#
#
# print(name)
# print('=='*10)



# With Global
# name = 'Momo'

# def grading():
#     global name
#     name = 'Kimsour'
#     grade = 'A'
#     age = 25
#     print(name)
#     print(grade)
#     print(age)
#
# grading()
# print(name)           # name = kimsour because we use global
# print('=='*10)



# name = 'BiMo'
# def internship():
#     grade = 'B'
#     print(grade)
#
# internship()
# print(name)
# print('=='*10)



# function composition
# use output one function can be input of other function
# def grading(totalmark):
#     if totalmark > 85:
#         return 'A'
#     elif totalmark >50:
#         return 'B'
#     else:
#         return 'F'
#
# def findtotal(marks):
#     total_mark = sum(marks)
#     return total_mark
#
# list_of_marks = [35,20,35,3]
# print(grading(findtotal(list_of_marks)))




# Recursive Function: A function that call itself
# def test():     # loop forever
#     print('Helllo')
#     test()
# test()

# def test():
#     print('Helllo')
#     test()


# 11/06/2021
# def print_n_times(name,n):
#     print(name,":",n)
#     if n == 0:
#         return
#     print_n_times(name, n-1)   # start from 10 to 0
# print_n_times("Seanghor",10)


# print('=='*10, 'Reverse')
# def print_n_times(name,n):
#     print(name, ":", n)
#     if n == 10:                 # when n = 10 it will stop loop
#         return
#     print_n_times(name, n+1)    # Start from 0 to 10
# print_n_times("Seanghor", 1)
#
#
#
# print('=='*10)
# i = 0
# def name_n_times(name, n):
#     global i
#     i += 1
#     print(f'{i}: {name}')
#     if n == 1:
#         return
#     name_n_times('Seanghor', n-1)
# name_n_times('Seanghor', 10)


# Factorial
# def find_factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n*(find_factorial(n-1))
# print('Factorial of 5: ', find_factorial(5))



# Noted
# import string
# digits = string.digits
# ascii_letter = string.ascii_letters
# hex_digits = string.hexdigits
# oct_digit = string.octdigits
# printable = string.printable
# lower_letters = string.ascii_lowercase
# upper_letters = string.ascii_uppercase
#
# print(f'digits: {digits}')
# print(f'ascii_letters: {ascii_letter}')
# print(f'hex_digits: {hex_digits}')
# print(f'oct_digit: {oct_digit}')
# print(f'printable: {printable}')
# print(f'lower_letters: {lower_letters}')
# print(f'upper_letters: {upper_letters}')



# import string
# def find_num(n):
#     non_num = []
#     if n.isdigit():
#         num = int(n)
#         print(num*10)
#     else:
#         for i in n:
#             if i not in string.digits:
#                 non_num.append(i)
#         print('The following are not numbers and can not be convered...',non_num)
#
# find_num('100seanghor433')
# find_num('5')
# find_num('hor')



# def linear_search(list, s_no):
#     pos = -1
#
#     for i in range(len(list)-1):
#         if s_no == list[i]:
#             return i
#     return pos
#
# res = linear_search([21,2,43,52,13,433,475], 42)
# if res == -1:   # res = pos = -1
#     print('Number not found in the list')
# else:
#     print('Number found at ', res)    # res = i
# print('=='*10)



# def linear_search(list, s_no):
#     for i in range(len(list)-1):
#         if s_no == list[i]:
#             return f'Number found at {i}'
#     return f'Number not found in the list'
#
# print(linear_search([50,65,123,23,12],65))
# print(linear_search([50,65,123,23,12],541))
# print('=='*10)


# def linear_search(list, s_no):
#     if s_no in list:
#         return f"Number found at: {list.index(s_no)}"
#     else:
#         return "Number not found in the list"
# print(linear_search([50,12,123,23,65],0))
# print(linear_search([50,65,123,23,12],65))
# print('=='*10)




# 15/06
# Binary Search

# def binary_search(list, sno):
#     l_bound = 0
#     u_bound = len(list)-1
#     count = 0
#     while u_bound >= l_bound:
#         mid = (l_bound+u_bound)//2
#         if list[mid] == sno:
#             print("It took ", count, " Executions to check the entire list")
#             return mid
#         elif list[mid]<sno:
#             l_bound = mid + 1
#         else:
#             u_bound = mid - 1
#         count+=1
#     print("It took ",count, " Executions to check the entire list")
#     return -1
# list = []
# for i in range(100000000):
#     list.append(i)
# sno = 10000001




# def binary_search(list, sno):
#     l_bound = 0
#     u_bound = len(list)-1
#     count = 0
#     while u_bound >= l_bound:
#         mid = (l_bound+u_bound)//2
#         if list[mid] == sno:
#             print("It took ", count, " Executions to check the entire list")
#             return mid
#         elif list[mid]<sno:
#             l_bound = mid + 1
#         else: # list[mid] > sno
#             u_bound = mid - 1
#         count+=1
#     print("It took ",count, "Executions to check the entire list")
#     return -1
#
# # pos = binary_search([5,10,11,13,27,48,77], 77)
# pos = binary_search([5,10,11,13,27,48,77], 10)
#
# if pos == -1:
#     print("Element not found")
# else:
#     print("Element found at index: ", pos)




# def binary_search(list, sno):
#     l_bound = 0
#     u_bound = len(list)-1
#     count = 0
#
#     while u_bound >= l_bound:
#         mid= (l_bound+u_bound)//2
#         if list[mid] == sno:
#             print("It took", count, "execution to check the entire list")
#             return mid
#         elif list[mid]>sno: #lower to higher use <, higher to lower use >
#             l_bound = mid+1
#         else:
#             u_bound = mid-1
#         count += 1
#     print("It took", count, "execution to check the entire list")
#     return -1
#
# list= [99,87,56,34,28,20,15]
# sno= 56
# pos= binary_search(list,sno)
#
# if pos == -1:
#     print("Element is not found")
# else:
#     print("Element is found at:", pos)




#22/06/2021
# def insection_sort(arr):
#     for i in range(len(arr)):
#         j=i
#         while arr[j]<arr[j-1] and j>0: # while arr[j]>arr[j+1] and j>=0:
#             arr[j],arr[j-1]=arr[j-1],arr[j]
#             # temp=arr[j]
#             # arr[j]=arr[j-1]
#             # arr[j-1]=temp
#             #
#             # arr[j]=arr[j]+arr[j-1]
#             # arr[j-1]=arr[j]-arr[j-1]
#             # arr[j]=arr[j]-arr[j-1]
#             j-=1
#
# arr=[12,10,5,3,55,45]
# print(arr)
# insection_sort(arr)
# print(arr)



# def sellection_sort(arr):
#     for i in range(len(arr)):
#         min_pos=i
#         for j in range(i,len(arr)):
#             if arr[j]<arr[min_pos]:
#                 min_pos=j
#         arr[i],arr[min_pos]=arr[min_pos],arr[i]
#         print(arr)
#
# arr=[12,10,5,3,55,45]
# print(arr)
# sellection_sort(arr)
# print(arr)




# def merge_sort(lists):
#     # Get the length of the list
#     len_list = len(lists)
#     # if the list only have only one element, the list is sorted
#     if len_list==1:
#         return lists
#     # Find the list element to split the list
#     mid = len_list//2
#     left_lists = merge_sort(lists[:mid])       # from line number 349 to 359 is used to divide list each time until it become one single separate list
#     right_lists = merge_sort(lists[mid:])
#     return merge(left_lists,right_lists)

# def merge(list1,list2):
#     i = j = 0
#     merge_list = []
#     len_list1 = len(list1)
#     len_list2 = len(list2)
#     while i < len_list1 and j < len_list2:
#         if list1[i] <= list2[j]:
#             merge_list.append(list1[i])
#             i+=1
#             print(f'list1:{merge_list}')
#         else:
#             merge_list.append(list2[j])           # from line number 361 to 377 is used to sort list and collect them again
#             j+=1
#             print(f'list2:{merge_list}')
#     merge_list.extend(list1[i:])
#     merge_list.extend(list2[j:])
#     return merge_list
#
#
# lists=[5,12,13,18,20,21,11,14,15,19,22,7]
# res=merge_sort(lists)
# print(merge_sort(res))



# def merge(list1,list2):
#     i = j = 0
#     merge_list = []
#     len_list1 = len(list1)
#     len_list2 = len(list2)
#     while i < len_list1 and j < len_list2:
#         if list1[i] <= list2[j]:
#             merge_list.append(list1[i])
#             i+=1
#             print(f'list1:{merge_list}')
#         else:
#             merge_list.append(list2[j])
#             j+=1
#             print(f'list2:{merge_list}')
#     return merge_list
#
#
# list1=[5,12,13,18,20,21]
# list2=[7,11,14,15,19,22]
# print(merge(list1,list2))
#

# or u can code
# def merge(list1, list2):
#     mergeList = list1 + list2
#     return sorted(mergeList)
# list1 = [5, 12, 13, 18]
# list2 = [7, 11, 14, 19]
# print(merge(list1, list2))



# task 3
# def merge(list1,list2):
#     i = j = 0
#     merge_list = []
#     len_list1 = len(list1)
#     len_list2 = len(list2)
#     while i < len_list1 and j < len_list2:
#         if list1[i] <= list2[j]:
#             merge_list.append(list1[i])
#             i+=1
#             #print(f'list1:{merge_list}')
#         else:
#             merge_list.append(list2[j])
#             j+=1
#             #print(f'list2:{merge_list}')
#     merge_list.extend(list1[i:])
#     merge_list.extend(list2[j:])
#     return sorted(merge_list)


# list1=[5,40,13,20,22,9,80,30,21]
# list2=[7,11,4,40,25,22]
# print(merge(list1,list2))
#


# # task4
# def merge_sort(lists):
#     if len(lists)==1:
#         return lists
#     mid = len(lists)//2
#     left_lists = merge_sort(lists[:mid])       # from line number 349 to 359 is used to divide list each time until it become one single separate list
#     right_lists = merge_sort(lists[mid:])
#     return merge(left_lists,right_lists)
#
# def merge(list1,list2):
#     i = j = 0
#     while i < len(list1) and j < len(list2):
#         if list1[i] <= list2[j]:
#             return sorted(list1[:i])
#         i+=1
#         else:
#             return sorted(list2[j:])  # from line number 361 to 377 is used to sort list and collect them again
#         j+=1
#
#
# lists=[5,12,13,18,20,21,11,14,15,19,22,7]
# res=merge_sort(lists)
# print(merge_sort(res))



# def quicksort(left,arr,right):   # left start from 0, right is the len(arr)-1
#     if left < right:
#         partition_pos = partition(left,arr,right)
#         quicksort(left,arr,partition_pos-1)  # call quicksort in all element which are less than pivot
#         quicksort(partition_pos+1,arr,right) # call quicksort in all element which are greater than pivot
#
# def partition(left,arr,right):   # this function is used to return  the index of the pivot element after the first step of quick sort
#     i = left
#     j = right
#     pivot = arr[right]
#
#     while i < j:
#         while i < right and arr[i] < pivot:  # means if value of i smaller than the value of pivot and position of i smaller than position of pivot then i need to manually move forward
#             i+=1
#         while j > left and arr[j] >= pivot:   # means if value of j greater than the value of i and position of j is greater or equal to position of pivot
#             j-=1
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#         print("right",j)
#     if arr[i] > pivot:
#         arr[i], arr[right]= arr[right], arr[i]
#
#     return i
#
# arr=[15,60,9,51,75,12,36,85,90]
# quicksort(0,arr,len(arr)-1)
# print(arr)



#Method number 2
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot=arr.pop()
#
#     item_greater = []
#     item_lower = []
#     for item in arr:
#         if item < pivot:
#             item_lower.append(item)
#         else:
#             item_greater.append(item)
#
#     return quick_sort(item_lower)+[pivot]+quick_sort(item_greater)      # it will repeat sorted the element and go over and over just like loop function
#
#
# print(quick_sort([15,60,9,51,75,12,36,85,90]))


# a= int(input("Enter a number:"))
# b= int(input("Enter another number:"))
# if a>0 and b>0:
#     c=a/b
#     print("Result:",c)
# else:
#     try:
#         c=a//b
#     except:
#         print("Divided zero issue, your input is wrong")
#     print("Success")
#
# a= int(input("Enter a number:"))
# b= int(input("Enter another number:"))
#
# print("Input successful")
# try:
#     print("Before the probematic code")
#     c=a/b
#     print("After the probematic code")
# except Exception as d:
#     print("The error is :",d)
# else:
#     print("No exception")
# print("Success")



# try:
#     a= int(input("Enter a number:"))
#     b= int(input("Enter another number:"))
#     c=a/b
#     print("Input successful")
# except Exception as d:
#     print("The error is :",d)
# else:
#     print("No exception")
# finally:
#     print("Don't worry")


print("You are trying to open the file")
try:
    file=open("file1.txt","r")
    print("Reading from the file")
except IOError as error:
    print("Unable to work with the file", error)
finally: # We use finally to release / close the resources
    print("File closed Successully")

print("Success...")

