msg=input("Input a text:")
if len(msg)<0:
    print("The string is empty")
else:
    first_half=msg[:len(msg)//2]
    second_half=msg[len(msg)//2:]
    first=first_half[::-1]
print(first+"  "+second_half)
