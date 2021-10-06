print("Input a number:")
num=input()
if num.isdigit():
    if int(num)%2!=0:
        print("The number you have entered is Odd")
    elif int(num)%2==0:
        print("The number you have entered is Even")
else:
    print("Not a valid Number")
