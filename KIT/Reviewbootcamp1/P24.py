import random
mytuple=[]
def random_tuple(time):
    for i in range(1,time+1):
        num=random.randint(0,100)
        print(f'Random{i}:',num)
        mytuple.append(num)
    print(tuple(mytuple))
    print(sum(mytuple))


random_tuple(5)
