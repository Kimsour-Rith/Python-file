import timeit
timeTakenForList = timeit.timeit(stmt ='[35,23,43,76,58,67]', number= 5000000)
timeTakenForSet = timeit.timeit(stmt='[35,23,43,76,58,67]', number= 5000000)
if(timeTakenForList-timeTakenForSet>0):
    print('Study more')
elif(timeTakenForList-timeTakenForSet<0):
    print('work harder')
else:
    print('Enjoy weekend')
