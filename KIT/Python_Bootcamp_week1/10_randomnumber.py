import random
number=random.randint(2000,3000)
n = int(input("Input Number:"))
even_random_Sum=0
for i in range(1,n+1):
     if (i%2==0):
          even_random_Sum+=(number)
print("Sum of even random numbers:",even_random_Sum)
