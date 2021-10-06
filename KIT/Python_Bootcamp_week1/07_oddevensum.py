inp= input("Input a number:")
oddSum=0
evenSum=0
if inp.isdigit():
    for k in range(1,int(inp)+1):
        if (k%2!=0):
            oddSum+=k
    print("Sum of odd number={1}".format(k,oddSum))
    for j in range(1,int(inp)+1):
        if(j%2==0):
             evenSum+=j
    print("Sum of even number={1}".format(j,evenSum))
else:
    print("Invalid number")
    print("Sum of odd number=0")
    print("Sum of even number=0")
