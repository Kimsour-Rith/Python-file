num=input("Input a number:")
oddSum=0
evenSum=0
if num.isdigit():
    covert=int(num)
    for e in range(0,covert+1):
        if e%2==0:
            evenSum+=e
        else:
            oddSum+=e
    print("Sum of odd numbers=",oddSum)
    print("Sum of even numbers=",evenSum)

else:
    print("Invalid input")
    print("Sum of odd numbers=",oddSum)
    print("Sum of even numbers=",evenSum)


