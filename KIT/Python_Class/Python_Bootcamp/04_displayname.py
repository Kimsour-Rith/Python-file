name= input("Enter your name:")
num_of_time= int(input("Enter number of times to display:"))
for i in range(num_of_time):
    print(name)
if not name:
    print('No name entered')
