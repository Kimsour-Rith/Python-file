print("python 08_oddevenaverage.py")
num= input("Input a number")
oddSum=0
evenSum=0
if num.isdigit():
    for i in range(1,int(num)+1):
        if i%2!=0:
            oddSum+=int(num)
            odd_average=oddSum//int(num)
    print("Average of odd numbers="+str(odd_average))
    for j in range(1,int(num)+1):
        if j%2==0:
            evenSum+=int(num)
            even_average= evenSum//int(num)
    print("Average of even numbers="+str(even_average))
else:
    print("Invalid Input")

