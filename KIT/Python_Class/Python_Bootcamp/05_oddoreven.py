num = input("Input a number:\n")
if num.strip().isdigit():   #Check if input is even number else it is odd number
    if int(num)%2 == 0:
        print("The number you have entered is Even")
    else:
        print(" The number you have entered is Odd ")
else:
    print("Not a valid number")






