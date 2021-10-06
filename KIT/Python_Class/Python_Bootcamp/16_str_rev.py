name = str(input("Input a string: "))
first_half,second_half = name[:len(name)//2],name[len(name)//2:]
first_half_length=len(first_half)
sliced_first_half = first_half[first_half_length::-1]
print(sliced_first_half+second_half)

if not name:
    print("The string is empty")
