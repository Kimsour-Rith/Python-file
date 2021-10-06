word = ""
sum = 0
while word != "stop":
    num = input("Input number: ")
    if num.isdigit():
        sum = int(num)+sum
    else:
        if num=="stop":
            print("Sum",sum)
            break
        else:
            print("The number must be a valid number")




