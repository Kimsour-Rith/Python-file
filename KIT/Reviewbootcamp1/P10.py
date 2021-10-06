import random
num=random.randint(2000,3000)
even_sum=0
inp=int(input("Input Number:"))
for i in range(1,inp+1):
    if i%2==0:
        even_sum+=num
print("Sum of even random numbers:",even_sum)
