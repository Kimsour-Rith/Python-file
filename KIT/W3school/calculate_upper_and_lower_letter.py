# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters
# def count_letter(strings):
#     count = {"Upper Case":0,"Lower Case":0}
#     for i in strings:
#         if i.isupper():
#             count["Upper Case"] += 1
#         elif i.islower():
#             count["Lower Case"] += 1
#         else:
#             pass
#     print("The number of Upper Case is: ",count["Upper Case"])
#     print("The number of Lower Case is: ",count["Lower Case"])
#
#
# count_letter("My name is Kimsour")





def count_string(strings):
    count_Upper = 0
    count_lower = 0
    for i in strings:
        if i.isupper():
            count_Upper += 1
        elif i.islower():
            count_lower += 1
        else:
            pass
    print("The number of Upper Case is: ", count_Upper)
    print("The number of Lower Case is: ",count_lower)


count_string("I am a Student")