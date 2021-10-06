num1 = 50
num2 = 6

res = num1 + num2
print(f'Sum = {res}') # Formatted String

res = num1 - num2
print('Difference = '+str(res))  # Concatenation 'Difference = ' + '300'

res = num1 * num2
print(f' {num1} * {num2} = {res}') # Convenient to inject the values into the string
print('num1*num2 ', num1, num2, res) # Older way 'num1*num2 ' => 'num1*num2 50' => 'num1*num2 506' => 'num1*num2 506300'

res = num1 / num2
print(f'Decimal quotient = {res} ')

res = num1 // num2
print(f'Integer quotient = {res}')

res = num1 % num2
print(f'Remainder = {res}')

res = num1 ** num2
print(f'Power = {res}')

name = "Kimsour"

print(f'Hello world my name is {name}' ) # We use { } to inject a variable into a String