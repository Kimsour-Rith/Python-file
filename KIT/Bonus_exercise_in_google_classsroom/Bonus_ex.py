import random
secret_num = random.randint(1,10000)
guess_count = 1
guess_limit = 6
while True:
    name=input("Please input your name before start the game: ")
    print("Hey",name,"are you ready to take the challenge? Press y/Y to start any other key to stop:")
    respond=input()
    if respond=="y"or respond=="Y":
            print("I have a number in mind (1 to 10000) you have maximum 6 attempts to guess the number")
            while guess_count<guess_limit:
                guess=int(input(f"Attempt{guess_count}="))
                if guess == secret_num:
                    print("Brilliant!",name,"you have guessed it in",guess_count,"attempts")
                    break
                elif guess>secret_num:
                    print(f'Attempt{guess_count} failed,guess a number lesser than that')
                else:
                     print(f'Attempt{guess_count} failed,guess a number higher than that')
                guess_count+=1
                if guess_count==guess_limit:
                    guess=int(input("Your last chance Attempt 6:"))
                    if guess==secret_num:
                        print("Brilliant!",name,"you have guessed it in",guess_count,"attempts")
                        break
                    else:
                        print(f" Attempt 6 failed,The number I have guessed was {secret_num}")
                        print("You have lost all your chances Better luck next time :(")
                        break

    elif respond == "n" or respond == "N":
        break

    print("Press y/Y if you want to restart the game n/N to quit:")
    inp1=input()
    if inp1=="n" or inp1=="N":
        break
    else:
        continue
