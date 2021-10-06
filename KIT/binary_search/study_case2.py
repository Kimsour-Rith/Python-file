# Theavuth Code
# introduction = "Welcome to the dice game!"
# print(introduction)
# while True:
#     dice_list = []
#     number_of_dice = input("Enter the number of dice: ")
#     if number_of_dice == "" or number_of_dice.isalpha():
#         print("USAGE: The number must be between 1 and 8")
#     elif number_of_dice.isdigit():
#         number_of_dice = int(number_of_dice)
#         if number_of_dice > 8 or number_of_dice == 0:
#             print("USAGE: The number must be between 1 and 8")
#         else:
#             number_of_dice = int(number_of_dice)
#             import random
#             for i in range(0, number_of_dice):
#                 dice_number = random.randint(1, 6)
#                 dice_list.append(dice_number)
#                 print(f"Dice {i + 1} : {dice_list[i]}")
#             print("=========")
#             print(f"Result: {sum(dice_list)}")
#             print("=========")
#             break





# Kimsour code
introduction = "Welcome to the dices games!"
print(introduction)
import random
while True:
    num = input("Enter a number of dices you want to roll: ")
    if num.isalpha() or num == "":
        print("USAGE: The number must be between 1 and 6")
        continue
    elif num.isdigit():
         num= int(num)
         if num < 1 or num > 8:
             print("USAGE: The number must be between 1 and 6")
         else:
             sum = 0
             for i in range(1,num+1):
                 rannum = random.randint(1, 8)
                 print(f'Dice{i}:',rannum)
                 sum += rannum
             print("\n"+"="*10+"\n")
             print("RESULT:",sum)
             print("\n"+"="*10)
             break



