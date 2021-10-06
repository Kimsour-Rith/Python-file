# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_element(lists):
    new_list=set(lists)
    return list(new_list)

print(unique_element([1,2,3,3,3,4,5,5,6]))
