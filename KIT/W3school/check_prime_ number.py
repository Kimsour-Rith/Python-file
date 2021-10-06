# Write a Python function that takes a number as a parameter and check the number is prime or not.
def prime(number):
    x = []
    for i in range (1,number+1):
        if number % i == 0:
            x.append(i)
    if len(x) > 2:
         print(number, "is not a prime number")
    elif len(x) == 2:
        print(number," is a prime number")
    else:
        print(number,"is not a prime number")

prime(-1)


