def binary_search(list,sno):
    l_bound=0
    u_bound=len(list)-1
    count=0
    while u_bound>=l_bound:
        mid=(l_bound+u_bound)//2
        if sno==list[mid]:
            print("It takes",count,"Time to iterate element in the list")
            return mid
        elif list[mid]<sno:
            l_bound=mid+1
            print("It takes",count,"Time to iterate element in the list")
        else:
            u_bound=mid-1
        count+=1
    print("It takes",count,"Time to iterate element in the list")
    return -1


list = []
for i in range(100000000):
    list.append(i)
sno = 10000001
pos = binary_search(list, sno)

if pos == -1:
    print("Element not found")
else:
    print("Element found at index: ", pos)
