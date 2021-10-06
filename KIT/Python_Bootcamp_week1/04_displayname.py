name= input("Enter your name:")
num_of_time= int(input("Enter number of times to display:"))
if len(name) <1 :
    print('No name entered')
else:
    for i in range(1, num_of_time):
        print(name)

