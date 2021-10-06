i=""
while i!="stop":
    name=input("Input your name")
    if name.isalpha():
        for i in name:
            sum(map(ord(i), name))
            print(sum)
    elif name.isalnum():
        print("Invalid String can't be converted")
    else:
        print("You asked to stop the program....Stopping")



