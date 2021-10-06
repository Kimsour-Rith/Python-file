def selection_sort(arr):
    for i in range(len(arr)):
        min_pos = i
        for j in range(i, len(arr)):
            if arr[j] > arr[min_pos]:  # Big to small
            # if arr[j] < arr[min_pos]: # Small to big
                min_pos = j
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
        print(arr)                     # to know how it change

arr = [12,10,5,3,55,45]
# print(arr)
selection_sort(arr)
print(arr)


# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_pos = i
#         for j in range(i+1, len(arr)):
#             if arr[j] > arr[min_pos]:  # Big to small
#             # if arr[j] < arr[min_pos]: # Small to big
#                 min_pos = j
#         arr[i], arr[min_pos] = arr[min_pos], arr[i]
#         # print(arr)    # to know how it change
#
# arr = [12,10,5,3,55,45]
# print(arr)
# selection_sort(arr)
# print(arr)
