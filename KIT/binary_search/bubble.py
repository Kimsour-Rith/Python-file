def bubble_sort(list):
    for i in range(len(list)-1,0,-1):
        print(i)
        for j in range(i):
            print(j)
            if list[j]>list[j+1]:
                temp = list[j]
                list[j] = list[j+1]     # or you can write list[j], list[j+1} = list[j+1], list[i]
                list[j+1] = temp
            print(list)
        print('*'*10)

list = [50,65,8,12,65,7]
bubble_sort(list)
print(list)
