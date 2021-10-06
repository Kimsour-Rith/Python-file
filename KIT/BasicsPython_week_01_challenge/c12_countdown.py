countdown=int(input("Enter a number:"))
if countdown<0:
    pass
else:
    for i in reversed(range(1,countdown+1)):
        print(i)
    print("BOOM!")
