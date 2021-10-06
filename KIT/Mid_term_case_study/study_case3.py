import random

print('Welcome to the dices game!')

x = input('Enter the number of the dices you want to roll: ')
result = 0
if x.isdigit() == False:
    print('USAGE: The number must be between 1 and 8')
    x = input('\nEnter the number of the dices you want to roll: ')
    for i in range(1,int(x)+1):
        ranNum = random.randint(1,6)
        print(f'Dice {i} : ',ranNum)
        result += ranNum
    print(f'='*10,'\nRESULT:',result)
    print(f'='*10)
else:
    for i in range(1,int(x)+1):
        ranNum = random.randint(1,6)
        print(f'Dice {i} : ',ranNum)
        result += ranNum
    print(f'='*10,'\nRESULT:',result)
    print(f'='*10)
