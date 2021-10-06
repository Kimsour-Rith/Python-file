def merge_sort(lists):
    # Get the length of the list
    len_list = len(lists)
    # if the list only have only one element, the list is sorted
    if len_list==1:
        return lists
    # Find the list element to split the list
    mid = len_list//2
    left_lists = merge_sort(lists[:mid])       # from line number 349 to 359 is used to divide list each time until it become one single separate list
    right_lists = merge_sort(lists[mid:])
    return merge(left_lists,right_lists)

def merge(list1,list2):
    i = j = 0
    merge_list = []
    len_list1 = len(list1)
    len_list2 = len(list2)
    while i < len_list1 and j < len_list2:
        if list1[i] <= list2[j]:
            merge_list.append(list1[i])
            i+=1
            print(f'list1:{merge_list}')
        else:
            merge_list.append(list2[j])           # from line number 361 to 377 is used to sort list and collect them again
            j+=1
            print(f'list2:{merge_list}')
    merge_list.extend(list1[i:])
    merge_list.extend(list2[j:])
    return merge_list


lists=[5,12,13,18,20,21,11,14,15,19,22,7]
res=merge_sort(lists)
print(merge_sort(res))



# def merge(list1,list2):
#     i = j = 0
#     merge_list = []
#     len_list1 = len(list1)
#     len_list2 = len(list2)
#     while i < len_list1 and j < len_list2:
#         if list1[i] <= list2[j]:
#             merge_list.append(list1[i])
#             i+=1
#             print(f'list1:{merge_list}')
#         else:
#             merge_list.append(list2[j])
#             j+=1
#             print(f'list2:{merge_list}')
#     return merge_list
#
#
# list1=[5,12,13,18,20,21]
# list2=[7,11,14,15,19,22]
# print(merge(list1,list2))
#

# or u can code
# def merge(list1, list2):
#     mergeList = list1 + list2
#     return sorted(mergeList)
# list1 = [5, 12, 13, 18]
# list2 = [7, 11, 14, 19]
# print(merge(list1, list2))



# task 3
# def merge(list1,list2):
#     i = j = 0
#     merge_list = []
#     len_list1 = len(list1)
#     len_list2 = len(list2)
#     while i < len_list1 and j < len_list2:
#         if list1[i] <= list2[j]:
#             merge_list.append(list1[i])
#             i+=1
#             #print(f'list1:{merge_list}')
#         else:
#             merge_list.append(list2[j])
#             j+=1
#             #print(f'list2:{merge_list}')
#     merge_list.extend(list1[i:])
#     merge_list.extend(list2[j:])
#     return sorted(merge_list)


# list1=[5,40,13,20,22,9,80,30,21]
# list2=[7,11,4,40,25,22]
# print(merge(list1,list2))
#


# # task4
# def merge_sort(lists):
#     if len(lists)==1:
#         return lists
#     mid = len(lists)//2
#     left_lists = merge_sort(lists[:mid])       # from line number 349 to 359 is used to divide list each time until it become one single separate list
#     right_lists = merge_sort(lists[mid:])
#     return merge(left_lists,right_lists)
#
# def merge(list1,list2):
#     i = j = 0
#     while i < len(list1) and j < len(list2):
#         if list1[i] <= list2[j]:
#             return sorted(list1[:i])
#         i+=1
#         else:
#             return sorted(list2[j:])  # from line number 361 to 377 is used to sort list and collect them again
#         j+=1
#
#
# lists=[5,12,13,18,20,21,11,14,15,19,22,7]
# res=merge_sort(lists)
# print(merge_sort(res))
