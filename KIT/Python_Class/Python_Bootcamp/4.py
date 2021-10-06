name=input("Input your name:")
num_of_time=int(input("Enter number of times to display:"))
if len(name)>1:
    for i in range(num_of_time):
        print(name)
else:
    print("No name entered")

