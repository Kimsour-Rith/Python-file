my_list = [50,55,7,85,9,10]
#Need to add a new element at the end of list

print(my_list)
#my_list.append([50,665])
print(my_list)

# Insert an element at a specific index
my_list.insert(0,65)
print(my_list)

# Removes an element passed in the arguments
my_list.remove(85)
print(my_list)

# Removes a particular element from the list if index specified

removed = my_list.pop(3)
print(my_list)
print(f'The pop() have removed {removed}')
# Removes the last element from the list if no idex specified

removed = my_list.pop()
print(f"The value removed was {removed}")

# Removes set of elements from your list
del my_list[0:2]
print(my_list)

# Add many elements at the end of list
my_list.extend([60,12,65,85,10])
print(my_list)

# Add elements at the beginning of the list as an element
#my_list.insert(0,[98,78,38,28])
print(my_list)

max_value = max(my_list)
print(max_value)

min_value = min(my_list)
print(min_value)

sum_values = sum(my_list)
print(sum_values)

my_new_list = sorted(my_list)
my_new_reversed_list = sorted(my_list, reverse=True)
print(my_new_list)
print(my_new_reversed_list)


names = ['Vignesh', 'Dinesh', 'Leo Fernandez','SopheapLiv']

names.sort(key=len)
print(names)


