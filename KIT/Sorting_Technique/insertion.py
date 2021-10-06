 # 22/06/
#insection sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j] > arr[j-1] and j>0:  # Big to small
            # temp = arr[i]
            # arr[j] = arr[j-1]
            # arr[j+1] = temp

            arr[j], arr[j-1] = arr[j-1], arr[j]   # can use this too
            j -= 1
arr = [12, 10, 5, 3, 55, 45]
print(arr)
print('=='*10)
insertion_sort(arr)
print(arr)



# def insertion_sort(arr):
#     for i in range(len(arr)):
#         j = i
#         while arr[j] < arr[j-1] and j>0:
#             arr[j], arr[j-1] = arr[j-1], arr[j]   # small to big
#
#             # Alternative codes for swapping
#             # temp = arr[j]
#             # arr[j] = arr[j+1]
#             # arr[j+2] = temp
#             #
#             # arr[j] = arr[j] + arr[j-1]
#             # arr[j-1] = arr[j] - arr[j-1]
#             # arr[j] = arr[j] - arr[j-1]
#             j -= 1
# arr = [12, 10, 5, 3, 55, 45]
# print(arr)
# insertion_sort(arr)
# print(arr)


# def insertion_sort(arr):
#     for i in range(len(arr)):
#         j = i
#         while arr[j] > arr[j-1] and j>0:
#             arr[j], arr[j-1] = arr[j-1], arr[j]   # can use this too
#             j -= 1
# arr = [12, 10, 5, 3, 55, 45]
# print(arr)
# insertion_sort(arr)
# print(arr)


# def insertion(arr):
#     for i in range(len(arr)-1):
#         while arr[i]> arr[i+1] and i>=0:
#             arr[i],arr[i+1] = arr[i+1],arr[i]
#             i-=1
#
# arr = [12,10,5,3,55,45]
# insertion(arr)
# print(arr)
