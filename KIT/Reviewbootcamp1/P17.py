msg=input("Input a string:")
if len(msg)<1:
    print("The string is empty")
else:
    first_char=msg[0]
    last_char=msg[-1]
    print("First Character:",first_char)
    print("Last Character:",last_char)
