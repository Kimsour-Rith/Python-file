#Exercise2: Write a Python function to sum all the numbers in a list

# def sum_list(lists):
#     sum = 0
#     for i in lists:
#         sum += i
#     return sum
#
# print(sum_list([2,3,4,5]))
#
# com = complex(3,5)
# print(com)
# com1 =
#
# point = float(input("ENter number:"))
# for k in range(0,1):
#     if point >= 0.9:
#         print('A')
#     elif point >= 0.8:
#         print('B')
#     elif point >= 0.7:
#         print('C')
#     elif point >= 0.6:
#         print('D')
#     elif point < 0.6:
#         print('F')
#     else:
#         print('Error')
# else:
#     print('Error')
#

#exercise 9
user_input = int(input("Enter a number: "))
odd =[]
even =[]
sum_odd=0
sum_even =0
for i in range(0,user_input+1):
    if int(i)%2 == 0:
        even.append(i)
        sum_even += i
    else:
        odd.append(i)
        sum_odd += i

print("Sum of even number: ",sum_even)
print("Sum of odd number: ",sum_odd)

#exercise 8
inp = int(input("Input a number: "))
while inp != "done" or "Done":
