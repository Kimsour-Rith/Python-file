def mean_of_list(list1):
    mylist=[item for item in list1]
    average=sum(mylist)/len(mylist)
    print(average)
    return average


mean_of_list([50,10,62,32])
