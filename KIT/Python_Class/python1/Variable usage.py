name = input("My name is:")
age = input("your age is:")
print(f"Your name is", name, "and you are beautiful and smart",f"and you are", age, "years old" )
number1 = input("number 1")
number2 = input("number2")
print("number 1:", number1,"number 2:", number2)

result = number1 + number2
print("Result :", result) # It will show as string not addition between those numbers

number1 = int(number1)
number2 = int(number2)
result = number1 + number2
print("Result:", result) # When you use int, it will show the result of total number

number1 = float(number1)
number2 = float(number2)
result = number1 + number2
print("Result:", result)
