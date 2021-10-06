msg=input("Enter a string: ")
first_half = msg[0:len(msg)//2]
second_half = msg[len(msg)//2:]
print(first_half.upper()+second_half.lower())
if not msg:
    print("The string is empty.")
