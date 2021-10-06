def quicksort(left,arr,right):   # left start from 0, right is the len(arr)-1
#     if left < right:
#         partition_pos = partition(left,arr,right)
#         quicksort(left,arr,partition_pos-1)  # call quicksort in all element which are less than pivot
#         quicksort(partition_pos+1,arr,right) # call quicksort in all element which are greater than pivot
#
# def partition(left,arr,right):   # this function is used to return  the index of the pivot element after the first step of quick sort
#     i = left
#     j = right
#     pivot = arr[right]
#
#     while i < j:
#         while i < right and arr[i] < pivot:  # means if value of i smaller than the value of pivot and position of i smaller than position of pivot then i need to manually move forward
#             i+=1
#         while j > left and arr[j] >= pivot:   # means if value of j greater than the value of i and position of j is greater or equal to position of pivot
#             j-=1
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#         print("right",j)
#     if arr[i] > pivot:
#         arr[i], arr[right]= arr[right], arr[i]
#
#     return i
#
# arr=[15,60,9,51,75,12,36,85,90]
# quicksort(0,arr,len(arr)-1)
# print(arr)



#Method number 2
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot=arr.pop()
#
#     item_greater = []
#     item_lower = []
#     for item in arr:
#         if item < pivot:
#             item_lower.append(item)
#         else:
#             item_greater.append(item)
#
#     return quick_sort(item_lower)+[pivot]+quick_sort(item_greater)      # it will repeat sorted the element and go over and over just like loop function
#
#
# print(quick_sort([15,60,9,51,75,12,36,85,90]))
