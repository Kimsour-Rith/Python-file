# Write a Python program to print the even numbers from a given list
def even_num(lists):
    x=[]
    for i in lists:
        if i % 2 == 0:
            x.append(i)
    return x

print(even_num([1,2,3,4,5,6,7,8]))