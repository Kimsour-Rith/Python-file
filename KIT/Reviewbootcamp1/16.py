string=input("Input a string:")
if len(string)<1:
    print("The string is empty")
else:
    first_half=string[:len(string)//2]
    second_half=string[len(string)//2:]
    print(first_half[::-1],second_half[::-1])
