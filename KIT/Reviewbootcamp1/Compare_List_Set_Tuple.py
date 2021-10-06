import sys,timeit
mytuple = ()
mylist = []
myset = {}

print('comparing the speed')

time_taken_for_tuple = timeit.timeit(stmt='(10,11,12,13,14,15,16)',number=1000000)
time_taken_for_list = timeit.timeit(stmt ='[10,11,12,13,14,15,16]',number=1000000)
time_taken_for_set = timeit.timeit(stmt= '{10,11,12,13,14,15,16}',number=1000000)

if time_taken_for_list>time_taken_for_tuple and time_taken_for_list>time_taken_for_set: print("cheetah")
elif time_taken_for_tuple>time_taken_for_set: print("Lion")
else: print("Tiger")
