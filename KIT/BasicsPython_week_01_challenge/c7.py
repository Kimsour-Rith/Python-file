def fine_factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*(fine_factorial(n-1))


print("Factorial of 10:", fine_factorial(10))
