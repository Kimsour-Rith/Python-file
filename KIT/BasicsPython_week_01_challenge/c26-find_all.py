def find_all(lists,value):
    if lists == []:
        return None
    elif value not in lists:
        return None
    else:
        start=-1
        my_list=[]
        while True:
            try:
                mylist=lists.index(value,start+1)
            except ValueError:
                break
            else:
                my_list.append(mylist)
                start=mylist
        return my_list

def find_first(list2,sno):
    for i in range(len(list2)-1):
        if sno==list2[i]:
            return list2.index(sno)
        else:
            return None


print(find_all([],1))
print(find_all(['Hello'],'Bye'))
print(find_all(['A','B','C','C','B','C','C'],'C'))
print(find_all([1,5,12,5,4],5))
print("*"*20)
print(find_first(['A','B','B','B','A'],'B'))
print(find_first(['100', '100', '200','300'], '100'))
