def make_dictionary(mylist,mytuple):
    list1=[item for item in mylist]
    tuple1=tuple([name for name in mytuple])

    mixvalue=zip(list1,tuple1)
    mydict=dict(mixvalue)
    print(mydict)
    return mydict


make_dictionary([50,10,62],("Borey","Thirak","Dane"))
