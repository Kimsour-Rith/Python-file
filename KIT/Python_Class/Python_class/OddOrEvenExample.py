number = int(input('Enter a number:'))

if number%2 == 0 and number %5==0:
    print('This is an even number and is divisible by 5')
elif number%2 == 0 and number %5!=0:
    print('Number is divisible by 2 but not by 5')
else:
    print('Odd Number')