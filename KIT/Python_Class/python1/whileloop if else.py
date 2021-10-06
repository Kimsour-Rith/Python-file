if 5 > 2:print("Five is greater than two!")
print("Yes") if 10<15 else print("No")

print("_"*50)
#Stop the loop if i is 3.
i = 0
while i < 10:
    i += 1
    if i == 3 :
        break
    print(i)

print("_"*50)
#In the loop, when i is 3, jump directly to the next iteration.
j = 0
while j < 6:
  j += 1
  if j == 3:
    continue
  print(j)
