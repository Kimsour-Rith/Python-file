import random
myTuple=[]
def random_tuple(time):
    for i in range(1,time+1):
        ran_num=random.randint(0,100)
        print(f'Random number {i}:{ran_num}')
        myTuple.append(ran_num)
    print(" ")
    print(tuple(myTuple))
    print(" ")
    print(sum(myTuple))
    return sum(myTuple)


random_tuple(5)
