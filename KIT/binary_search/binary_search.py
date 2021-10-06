def binary_search(list,sno):
    l_bound=0
    u_bound=len(list)-1
    count=0
    while u_bound>=l_bound:
        mid=(l_bound+u_bound)//2
        if sno==list[mid]:
            return mid
        elif list[mid]<sno:
            l_bound=mid+1
            print("It takes",count,"Time for execution ")
        else:
            l_bound=mid-1
    print("It takes",count,"Time for execution ")
    count+=1
    return -1

list=[12,13,45,87,85,90,67,87]
sno= 67
pos=binary_search(list,sno)

if pos==-1:
    print("The element is not found in list")
else:
    print("The element is found at index",pos)
