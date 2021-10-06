def sort_set(lists):
    print(sorted(list(set(lists)),reverse= False)) #list(set(lists)) is used to convert it to a set and then back into a list


sort_set([])
sort_set(['Hello'])
sort_set(['A','B','C','C', 'B'])
sort_set([1,5,12,5,4])
print("*"*20)

def sort_set_rev(lists1):
    print(sorted(list(set(lists1)),reverse=True))


sort_set_rev(['A','B','C','D','E'])
sort_set_rev(['100','100','200','300'])
sort_set_rev([1,5,12,5,4])
