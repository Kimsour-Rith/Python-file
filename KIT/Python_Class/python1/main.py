num1 = 50
num2 = 6
# This is a comment line and comment lines won't be executed by the interpreter
res = num1 + num2
print(f'Sum ={res}')
# Formatted String (Note: f with sum or f with difference are used with {})
res = num1 - num2
print(f'Apple ={res}')
# Concatenation => 'Difference = ' + '300' print('difference ='+ str(res))
res = num1 * num2
print(f' {num1} * {num2} = {res}')
# Convenient to inject the values into the string
print('num1 * num2 ', num1, num2, res)
res = num1 / num2
print(f'Decimal quotient = {res}')

res = num1 // num2
print(f'Integer quotient = {res}')
# we use f with string to make it as formatted string
res = num1 % num2
print(f'Remainder = {res}')

res = num1 ** num2
print(f'power = {res}')

name = "Kimsour"
print(f'Hello world my name is {name}')
# we use { } to inject a variable into a String


