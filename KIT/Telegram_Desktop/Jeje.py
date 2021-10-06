# Jesour
def merge_sort(list):
    # Get the length of list
    len_list = len(list)
    # If list having only 1 element, the list is sorted
    if len_list == 1:
        return list
    # Find the mid element to split the list
    mid = len(list)//2
    left_list = merge_sort(list[:mid])
    right_list = merge_sort(list[mid:])

    print(f'left {left_list}')
    print(f'right {right_list}')
    return merge(left_list, right_list)

def merge(list1, list2):
    i = j = 0
    merge_list = []
    len_list1 = len(list1)
    len_list2 = len(list2)

    while i < len_list1 and j < len_list2:
        if list1[i] < list2[j]:
            merge_list.append(list1[i])
            i += 1
        else:
            merge_list.append(list2[j])
            j += 1
    merge_list.extend(list1[i:])     # to insert another element
    merge_list.extend(list2[j:])
    print(f'Given {merge_list}')

    a = '##'*10
    print(f'{i} {a}')
    return merge_list


list = [21,11,14,5,12,13,20,19,15,17,22,7]   # left = [21,11,14,5,12,13], Right = [20,19,15,17,7,22]
res = merge_sort(list)
print(f'Finally Je Sour cute : {res}')
