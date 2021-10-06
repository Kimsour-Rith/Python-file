def quick_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr.pop()

    item_greater=[]
    item_lower=[]
    for item in arr:
        if item < pivot:
            item_lower.append(item)
        else:
            item_greater.append(item)

    return quick_sort(item_lower)+[pivot]+quick_sort(item_greater)      # it will repeat sorting the element and go over and over just like loop function


print(quick_sort([15,60,9,51,75,12,36,85,90]))
