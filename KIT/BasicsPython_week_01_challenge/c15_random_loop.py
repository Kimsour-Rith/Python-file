import random
inp=int(input("Enter a number:"))
if inp==0:
    pass
else:
    for i in range(1,inp+1):
        number=random.randint(0,1)
        print(number)
