number = int(input('Input a number:'))

if number%2 ==0:
    if number%5==0:
        print('Number is Even and also divisible by 5')
    else:
        print('Number is even but not divisible by 5')
else:
    if number%5==0:
        print('Number is odd and divisible by 5')
    else:
        print('Number is odd and not divisible by 5')