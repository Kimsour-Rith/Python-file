import sys,timeit
mytuple = (10,11,12,13,14,15,16)
mylist = [ 17,18,19,20,21,22,23]
myset = { 24,25,26,27,28,29,30}

print('comparing the size')
sizeoftuple = sys.getsizeof(mytuple)
sizeofmylist = sys.getsizeof(mylist)
sizeofmyset = sys.getsizeof(myset)

print('Size of tuple', sizeoftuple)
print('Size of list', sizeofmylist)
print('size of set', sizeofmyset)

print('comparing the speed')

time_taken_for_tuple = timeit.timeit(stmt='(10,11,12,13,14,15,16)',number=1000000)
time_taken_for_list = timeit.timeit(stmt ='[10,11,12,13,14,15,16]',number=1000000)
time_taken_for_set = timeit.timeit(stmt= '{10,11,12,13,14,15,16}',number=1000000)

print("Time taken for tuple:",time_taken_for_tuple)
print("Time taken for list :",time_taken_for_list)
print("Time taken for set :",time_taken_for_set)


