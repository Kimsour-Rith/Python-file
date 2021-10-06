myList1 = [50,52,9,'Test']
myTuple = (65,98,78,62,'Test')

myList1[0] = 150

#myTuple[0] = 500
# print(myList1)
# print(myTuple)
print("List methods")
print(dir(myList1))
help(myList1.insert)

print("Tuple methods")
print(dir(myTuple))
print(help(myTuple.__add__))
