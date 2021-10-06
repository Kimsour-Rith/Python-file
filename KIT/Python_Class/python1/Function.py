mylist = [30,90,50,60,75,25]
print(mylist)

mylist.append(888) # append is used to add a new element at the end of list
print(mylist)

mylist.insert(3,85) # insert is used to insert an element at a specific index
print(mylist)

mylist.remove(90) # removed is used to removes a  particular element from the list if index specified
print(mylist)

removed = mylist.pop(3) # is used to remove the last element from the list if no index specified.
print(mylist)
print(f'The pop() have removed {removed}')
print("_"*50)
mylist.pop(5)
print(mylist)

removed = mylist.pop()
print(f'The value removed was {removed}')

mylist.extend([12,13,14,15,1555]) # is used to add multiple elements at the end of the list
print(mylist)

del mylist[1:3] # is use to remove set of elements from your list
print(mylist)

min_value = min(mylist)
print(min_value)

max_value = max(mylist)
print(max_value)

sum_values = sum(mylist)
print(sum_values)


my_new_list = sorted(mylist)
print(mylist)
