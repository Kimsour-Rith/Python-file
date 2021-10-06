inp= input("Input a number:")
if inp.strip().isdigit():
    # check if input is even number else it is odd number
    if int(inp)%2==0:
        print('The number you  have entered is Even')
    else:
        print("The number you have entered is Odd")
else:
    print("Not a valid Number")
