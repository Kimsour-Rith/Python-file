# Write a Python function to multiply all the numbers in a list

def multiply(lists):
    mul = 1
    for i in lists:
        mul *= i
    return mul

print(multiply([2,3,4,5]))