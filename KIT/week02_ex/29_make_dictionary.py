def make_dictionary(mylist,myTuple):
    list1=[num for num in mylist]
    tuple1=[string for string in myTuple]
    mixvalue=zip(list1,tuple1)
    myNewDict=dict(mixvalue)
    print(myNewDict)
    return myNewDict


make_dictionary([50,10,62],("Borey","Thirak","Dane"))
