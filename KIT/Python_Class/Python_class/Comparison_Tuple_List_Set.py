import sys,timeit

myList = [25,65,95,87,52,62,'Hello']
myTuple = (25,65,95,87,52,62,'Hello')
mySet = {25,65,95,87,52,62,'Hello'}

sizeOfList = sys.getsizeof(myList)
sizeOfTuple = sys.getsizeof(myTuple)
sizeOfSet = sys.getsizeof(mySet)

print('Size of List: ', sizeOfList)
print('Size of Tuple: ', sizeOfTuple)
print('Size of Set: ', sizeOfSet)

print("Comparing the speed")

timeTakenForList = timeit.timeit(stmt='[35,23,43,76,58,67]', number=5000000)
timeTakenForTuple = timeit.timeit(stmt='(35,23,43,76,58,67)', number=5000000)
timeTakenForSet = timeit.timeit(stmt='{35,23,43,76,58,67}', number=5000000)

print("Time taken for List:", timeTakenForList)
print("Time taken for Tuple:", timeTakenForTuple)
print("Time taken for Set:", timeTakenForSet)

