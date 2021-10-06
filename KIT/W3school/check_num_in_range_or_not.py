# Write a Python function to check whether a number falls in a given range.
def check_num(n):
    if n in range(3,9):
        print (n, "is in range given")
    else:
        print("This number is not in range given")

check_num(2)