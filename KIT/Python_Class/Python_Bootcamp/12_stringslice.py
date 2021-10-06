name=input("Input a text:")

first_string,second_string= name[0:len(name)//2],\
                            name[len(name)//2:]
print(first_string+ "  ",second_string)

if not name:
    print("The string is empty")


