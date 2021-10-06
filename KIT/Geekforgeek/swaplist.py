#Given a list, write a Python program to swap first and last element of the list.
def swap_list(newlist):
    newlist[0],newlist[-1]=newlist[-1],newlist[0]
    return newlist
newlist=[12,34,56,67,98]
print(swap_list(newlist))
