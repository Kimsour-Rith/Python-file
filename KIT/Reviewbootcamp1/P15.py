string=input("Enter a string:")
if len(string)<1:
    print("The string is empty")
else:
    first=string[:len(string)//2]
    second=string[len(string)//2:]
    print(first.upper(),second.lower())
