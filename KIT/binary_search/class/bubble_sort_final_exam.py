def bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for k in range(i):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+ 1] = arr[k + 1], arr[k]
            print(arr)


list = [72,65,8,12,100,45]
bubble_sort(list)
print(list)