def selection_sort(arr):
    for i in range(len(arr)):
        min_pos = i
        for k in range(i, len(arr)):
            if arr[k] < arr[min_pos]:
                min_pos = k
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
        print(arr)

arr = [12,95,5,3,60,45]
selection_sort(arr)
print(arr)