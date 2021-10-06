# def sumofcollection(list_num):
#     return sum(list_num)
# result = sumofcollection([50,60,100,85,65])
# print(result)



# def ret_collection_from_fn(ran):
#     lists = []
#     for i in ran:
#         lists.append(i)
#     return lists
# print(ret_collection_from_fn('seanghor'))
# #print(ret_collection_from_fn(54))         # Error


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
#


# With Global
name = 'Momo'

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
# #list_of_marks = [35,20,35,3]
# print(grading(findtotal([35,20,35,3])))




# Recursive Function: A function that call itself
# def test():     # loop forever
#     print('Helllo')
#     test()
# test()                # in order to stop the loop you need to make a condition to stop
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
#
#
# print('=='*10, 'Reverse')
# def print_n_times(name,n):
#     print(name, ":", n)
#     if n == 10:                 # when n = 10 it will stop loop
#         return
#     print_n_times(name, n+1)    # Start from 0 to 10
# print_n_times("Seanghor", 1)



# print('=='*10)
i = 0
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
#     if n == 0 or n==1:
#         return 1
#     else:
#
#         return n*(find_factorial(n-1))  # 5*4*3*2*1
#
# print('Factorial of 5: ', find_factorial(5))
#



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
#             if i not in string.digits:              # digits: 123456789
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
# # res = linear_search([21,2,43,52,13,433,475], 42)
# res = linear_search([21,2,43,52,13,433,475], 13)
#
# if res == -1:   # res = pos = -1
#     print('Number not found in the list')
# else:   # res = i
#     print('Number found at ', res)    # res = i
# print('=='*10)
#


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

def binary_search(list, sno):
    l_bound = 0
    u_bound = len(list)-1
    count = 0
    while u_bound >= l_bound:
        mid = (l_bound+u_bound)//2
        if list[mid] == sno:
            print("It took ", count, " Executions to check the entire list")
            return mid
        elif list[mid]<sno:
            l_bound = mid + 1
        else:
            u_bound = mid - 1
        count+=1
    print("It took ",count, " Executions to check the entire list")
    return -1

# list = []
# for i in range(100000000):
#     list.append(i)
# sno = 10000001


def binary_search(list, sno):
    l_bound = 0
    u_bound = len(list)-1
    count = 0
    while u_bound >= l_bound:
        mid = (l_bound+u_bound)//2
        if list[mid] == sno:
            print("It took ", count, " Executions to check the entire list")
            return mid
        elif list[mid]<sno:
            l_bound = mid + 1
        else:       # list[mid] > sno
            u_bound = mid - 1
        count+=1
    print("It took ",count, "Executions to check the entire list")
    return -1

# pos = binary_search([5,10,11,13,27,48,77], 77)
pos = binary_search([5,10,11,13,27,48,77], 77)
#
if pos == -1:
    print("Element not found")
else:
    print("Element found at index: ", pos)



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
#         elif list[mid]<sno:         #lower to higher use <, higher to lower use >
#             l_bound = mid+1
#         else:
#             u_bound = mid-1
#         count += 1
#     print("It took", count, "execution to check the entire list")
#     return -1
#
# list = [99,87,56,34,28,20,15]
# sno= 87
# pos= binary_search(list,sno)
#
# if pos == -1:
#     print("Element is not found")
# else:
#     print("Element is found at:", pos)



 # 22/06/
# insection sort
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         j = i
#         while arr[j] > arr[j-1] and j>0:  # Big to small
#             # temp = arr[i]
#             # arr[j] = arr[j-1]
#             # arr[j+1] = temp
#
#             arr[j], arr[j-1] = arr[j-1], arr[j]   # can use this too
#             j -= 1
# arr = [12, 10, 5, 3, 55, 45]
# print(arr)
# print('=='*10)
# insertion_sort(arr)
# print(arr)



def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while arr[j] < arr[j-1] and j>0:
            arr[j], arr[j-1] = arr[j-1], arr[j]   # small to big

            # Alternative codes for swapping
            # temp = arr[j]
            # arr[j] = arr[j+1]
            # arr[j+2] = temp
            #
            # arr[j] = arr[j] + arr[j-1]
            # arr[j-1] = arr[j] - arr[j-1]
            # arr[j] = arr[j] - arr[j-1]
            j -= 1
arr = [12, 10, 5, 3, 55, 45]
print(arr)
insertion_sort(arr)
print(arr)


# def insertion_sort(arr):
#     for i in range(len(arr)):
#         j = i
#         while arr[j] < arr[j-1] and j>0:
#             arr[j], arr[j-1] = arr[j-1], arr[j]   # can use this too
#             j -= 1
# arr = [12, 10, 5, 3, 55, 45]
# print(arr)
# insertion_sort(arr)
# print(arr)


# def insertion(arr):
#     for i in range(len(arr)-1):
#         while arr[i]> arr[i+1] and i>=0:
#             arr[i],arr[i+1] = arr[i+1],arr[i]
#             i-=1
#
# arr = [12,10,5,3,55,45]
# insertion(arr)
# print(arr)

# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_pos = i
#         for j in range(i, len(arr)):
#             if arr[j] > arr[min_pos]:  # Big to small
#             # if arr[j] < arr[min_pos]: # Small to big
#                 min_pos = j
#         arr[i], arr[min_pos] = arr[min_pos], arr[i]
#         print(arr)                     # to know how it change
#
# arr = [12,10,5,3,55,45]
# # print(arr)
# selection_sort(arr)
# print(arr)


# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_pos = i
#         for j in range(i+1, len(arr)):
#             if arr[j] > arr[min_pos]:  # Big to small
#             # if arr[j] < arr[min_pos]: # Small to big
#                 min_pos = j
#         arr[i], arr[min_pos] = arr[min_pos], arr[i]
#         # print(arr)    # to know how it change
#
# arr = [12,10,5,3,55,45]
# print(arr)
# selection_sort(arr)
# print(arr)






# 02/07 #######################################################################################################################
# 01_Exception
# a = int(input("Input a number: "))
# b = int(input("Input a number: "))
#
# print("Input success")
# c = a/b               # this line can cause problem (Ex: if you input b = 0 then code will error)
# print("Result: ", c)



#
# a = int(input("Input a number: "))
# b = int(input("Input a number: "))
#
# print("Input success")
# try:
#     c = a/b              # this line can cause problem (Ex: if you input b = 0 then code will error)
# except:
#     print("Divide by Zero issue, your input is wrong")
# print("Result: ", c)


# Try and Except
# a = int(input("Input a number: "))
# b = int(input("Input a number: "))
#
# print("Input success")
# try:
#     print("Befor the probanatic code")
#     c = a/b              # this line can cause problem (Ex: if you input b = 0 then code will error)
#     print("After the probenatic code")
# except:                  # it will not work if there is no problem at (Try)
#      # if b = 0 => c = a/b is not work, (try block) will not work and (except block) will excuse
#      # if b != 0 => c = a/b is work, (try block) will work and (except block) will not excuse
#     print("Divide by Zero issue, your input is wrong")
#
#
#
# else:         # if Try block execuse it will execuse
#     print("No Exception")
# print("Result: ", c)




#
# a = int(input("Input a number: "))
# b = int(input("Input a number: "))
#
# print("Input success")
# try:
#     print("Before the probematic code")
#     c = a/b
#     print("After the probematic code")
# except Exception:
#     print("Input Error")
#     # if b = 0 => c = a/b is not work, (try block) will not work and (except block) will excuse
#     # if b != 0 => c = a/b is work, (try block) will work and (except block) will not excuse
#
# else:      # if Try block execuse it will execuse
#     print("No Exceptions")
# print("Success...")


## Except as Error
# a = int(input("Input a number: "))
# b = int(input("Input a number: "))
#
# print("Input success")
# try:
#     print("Before the probematic code")
#     c = a/b
#     print("After the probematic code")
# # except Exception as errorDetail:
# # except ioError as e:
#     print("The Error is: ",errorDetail)
#     # if b = 0 => c = a/b is not work, (try block) will not work and (except block) will excuse and information from try block will store in errorDetail
#     # if b != 0 => c = a/b is work, (try block) will work and (except block) will not excuse
#
# else:
#     print("No Exceptions")
# print("Success...")



# print("Trying to open a file")
# try:
#     f = open("test.txt", "r")                  # because i don't have this file name
#     print("Reading from the file")
# except IOError as error:
#     print("Unable to work with the file", error)
# finally: # We use finally to release / close the resources
#     print("File closed Successully")
#
# print("Success...")



#
# try:
#     a = int(input("Input a number: "))
#     b = int(input("Input a number: "))
#     c = a/b
#     print("No Problem in code")             # if c = a/b does not work => this not print
# except ZeroDivisionError as e:
#     print("Problem in code!!",e)
# finally:
#     print("Hello")
# print("Trying to open a file")




#
# try:
#     f = open("test1.txt", "r")
#     print("Reading from the file")
#
# except IOError as error:
#     print("Unable to work with the file", error)
#
# finally: # We use finally to release / close the resources
#     print("File closed Successully")
#
# print("Success...")




# try:
#     a = int(input("Input a number: "))
#     b = int(input("Input a number: "))
#     c = a/b
#     print("No Problem in code")
#     print("Result: ", c)
# except ZeroDivisionError as e:
#     print("Problem in code",e)
# finally:
#     print("Be happy")

# a= int(input("Input a number: "))
# b=int(input("Input another number:"))
# try:
#     c= a/b
#     f=open("testingpy.txt","r")
# except (ZeroDivisionError, IOError) as e:
#     print(e)
# finally:
#     print("Process finish")


# a= int(input("Input a number: "))
# b=int(input("Input another number:"))
# try:
#     c= a/b
#     f=open("testingpy.txt","r")
# except (ZeroDivisionError, IOError) as e:
#     print(e)
# #except FileNotFoundError as e:  # or you can use IOError as well, it also handle for file error
#     #print("File not found")
# finally:
#     print("Process finish")

# marks = int(input("Enter your marks"))
# try:
#     if marks > 100:
#         raise ArithmeticError
# except ArithmeticError:
#     print("The marks must lower than or equal to 100")




# marks = int(input("Enter your marks"))
# try:
#     if marks > 100:
#         raise Exception
#     elif marks >= 90:
#         print("Congratulation you pass grade : A")
#     elif marks >= 80:
#         print("Congratulation you pass grade : B")
#     elif marks >= 70:
#         print("Congratulation you pass grade : C")
#     elif marks >= 60:
#         print("Congratulation you pass grade : D")
#     elif marks >= 50:
#         print ("Congratulation you pass grade : E")
#     else:
#         print("Congratulation you pass grade : F")
#
# except Exception as e:
#     print("The marks must lower than or equal to 100")
# finally:
#     print("process finish")
#
# File_Heading_read
#f_control=open("E:/KIT/my1.txt", "r")
# mes3 = f_control.readline()
# print(mes3)
# message = f_control.read(5)
# print(message)
# mes1= f_control.readline(10)    # It doesn't matter if the variable are the same nor different
# print(mes1)
# msg = f_control.read()
# print(msg)
# for i in f_control:
#     print(i)


# with open("E:/KIT/my1.txt", "r") as file:       # work the same way as for i in file:
#     print(file.read())                                      # print(i)

# with open('E:/KIT/my1.txt', 'r') as f_control:
#     print(f_control.read())
#     print(f_control.readline())

    # print("=="*20)
    # l1 = f_control.read(4)
    # print(l1)


    # print("=="*20)
    # l = f_control.read()
    # print(l)
    #
    # print("=="*20)
    # r1 = f_control.readline(4)
    # print(r1)
    #
    # print("=="*20)
    # r = f_control.readline()
    # print(r)

# File Handing write mode
# try:
#     f = open("C:/Users/user/Desktop/test1.txt","w")
#     message = input("Input some text: ")
#     f.write(message)
# except:
#     print("Unable to open the file")        # The write mode clear anything before user writing the new text one
# finally:
#    f.close()
#    print("File closed successfully")

# File Handing Append

# try:
#     f = open("C:/Users/user/Desktop/test1.txt","a")
#     message ="\n" + input("Input some text: ")
#     f.write(message)
# except:
#     print("Unable to open the file")
# finally:
#    f.close()
#    print("File closed successfully")


#File Handing Write Read
# try:
#     f = open("C:/Users/user/Desktop/test1.txt","w+")   # w+ means write then read so after write the text, the read fuction will go to the end position of the text, and it it nothing
#     message= input( "Input some text: ")
#     f.write(message)
#     f.seek(0,0)
#     message = f.read()
#     print(message)
# except Exception as e:
#     print("Exception: ",e)
# finally:
#     f.close()
#     print("File closed successfully")

#File Handing Reand and Write
try:
    f= open("C:/Users/user/Desktop/test1.txt","r+")     # r+ means read then write
    message= "\n" +input("Input some text: ")           # after u input text it will read first then it eliminate the previous text by the number of characters that user input
    f.write(message)
    f.seek(0,0)
    message= f.read()
    print(message)
except Exception as e:
    print("Exception: ",e)
finally:
    f.close()
    print("File closed successfully")




# try:
#     f= open("C:/Users/user/Desktop/test1.txt","r+")     # r+ means read then write
#     message= "\n" +input("Input some text: ")       # after u input text it will read first then it eliminate the previous text by the number of characters that user input
#     f.seek(0,2)           # 2 means move the cursive to the last position of the text and move no character, don't move any character just stay here
#     f.write(message)
#     f.seek(0,0)           # move the cursive from the start and read from the start position
#     message= f.read()
#     print(message)
# except Exception as e:
#     print("Exception: ",e)
# finally:
#     f.close()
#     print("File closed successfully")


# File Handing Append Read
# try:
#     f= open("C:/Users/user/Desktop/test1.txt","a+")     # a+ means append then read
#     message= "\n" +input("Input some text: ")       # after u input text it will append more text and cursive will automatically go to the end of the text and start reading from the beginning of the new line
#     f.write(message)                                # therefore no need to call f.seek(0,2)
#     f.seek(0,0)     # move the cursive from the start and read from the start position
#     message= f.read()
#     print(message)
# except Exception as e:
#     print("Exception: ",e)
# finally:
#     f.close()
#     print("File closed successfully")




