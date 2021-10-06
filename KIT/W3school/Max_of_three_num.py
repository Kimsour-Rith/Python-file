#Exercise1 : Write a Python function to find the Max of three numbers.

def max_of_three(x,y,z):
    if x > y and x >z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z


result = max_of_three(3,9,-5)
print(result)


# def absolute_value(num):
#     """This function returns the absolute
#     value of the entered number"""
#     if num >= 0:
#         return num
#     return -num
#
#
# print(absolute_value(-2))
# print(absolute_value(6))

# def student_details(**args):
#     for key,value in args.items():
#         print(key,'=',value)
#     print("*"*10)
#     for i in args:
#         print(i)
# student_details(id=200,name='dog',age=16)
# print("*"*10)
# student_details(name='Cat',age=19,id=3000)

# def student_details(**args):
#     print(args)
    # for key,value in args.items():
        # print(key,' = ', value)

# student_details(id=200, name='Sreylin', age = 16)      # look like Dictionary but not coz Dict = {key:value}

#
#print('*'*10)
# student_details(name='Sovann', age=19, id=3000)

#
# print('*'*10)
# def student_details(*args):
#     print(args)
# student_details('hor', 123, 12345, 'BuBu')









####Loop For in Dictionary
#my_dict = dict(seanghor= 'pw12345', hor=12345, you=4567, dar=44444, srun=1111)          #{keys,values}
# for values in my_dict:
#      print(values)            #Output is Keys, not Values
#      print(my_dict[values])    #output is Values
# print('*'*20)
# for keys in my_dict:
#     print(keys)                  #output is Key(name)
#     print(my_dict[keys])         #Output is Values(pw)
#     print(keys, '=', my_dict[keys])
# print('*'*20)
# for i in my_dict:
#     print(i)                    #print(name) = key
# print('*'*20)
# for keys,values in my_dict.items():
#     print(keys, '=', values)
# print('*'*20)
# for items111 in my_dict.items():
    # print(items111)


# def student_details(**args):
#     print(args)
#     for key,value in args.items():
#         #print(key,' = ', value)
#         print(value)
#
# student_details(id=200, name='Sreylin', age = 16)      # look like


