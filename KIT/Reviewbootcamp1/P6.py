sum=0
user_inp=input("Input a number: ")
while user_inp!="Stop":
    if user_inp.isdigit():
        number=int(user_inp)
        sum += number
    else:
        print("The input must be a valid number")
    user_inp=input('Input a number: ')
print("Sum= ",sum)



