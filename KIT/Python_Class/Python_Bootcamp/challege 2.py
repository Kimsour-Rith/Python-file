import random
secret_num = random.randint(1,10000)
guess_count = 1
guess_limit = 7
while True:
    name=input("Please input your name before start the game: ")
    print("Hey",name,"are you ready to take the challenge? Press y/Y to start any other key to stop:")
    respond=input()
    if respond=="n" or respond=="n":
        break
    else:
        if respond == "y"or respond == "Y":
            print("I have a number in mind (1 to 10000) you have maximum 6 attempts to guess the number")
            while guess_count<guess_limit:
                guess=int(input(f"Attempt{guess_count}="))
                if guess == secret_num:
                    print("Brilliant!",name,"you have guessed it in",guess_count,"attempts")
                    print("Pres y/Y if you want to restart the game n/N to quit:")
                    respond=input()
                    if respond == "n" or respond=="N":
                        break
                    else:
                        continue


                else:
                    if guess>secret_num:
                        print(f'Attempt{guess_count} failed,guess a number lesser than that')
                        guess_count+=1
                    elif guess<secret_num:
                        print(f'Attempt{guess_count} failed,guess a number higher than that')
                        guess_count+=1
                    if guess_count==guess_limit-1:
                        inp=input("Your last chance Attempt 6:")
                        if inp!=secret_num:
                            print(f"\n\n Attempt 6 failed,The number I have guessed was {secret_num}")
                            print("\n\nYou have lost all your chances Better luck next time :(")
                            print("Pres y/Y if you want to restart the game n/N to quit:")
                            respond=input()
                            if respond == "n" or respond=="N":
                                break
                            else:
                                continue

















