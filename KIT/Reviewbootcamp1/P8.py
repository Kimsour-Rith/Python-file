num=input("Input a number:")
oddSum=0
evenSum=0
if num.isdigit():
    convert=int(num)
    for e in range(0, convert):
        if e%2==0:
            evenSum+=convert
            average_even=evenSum//convert
        else:
            oddSum+=convert
            average_odd=oddSum//convert
    print("Average of odd numbers=",average_odd)
    print("Average of even numbers=",average_even)

else:
    print("Invalid input")
