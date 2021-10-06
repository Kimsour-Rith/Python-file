def search_in_tuple(tuple1,arg):
    myTuple=(tuple(tuple1))
    if arg in myTuple:
        index1=myTuple.index(arg)
        print(f'Element found at Index:{index1}')
        return index1
    else:
        print("Element not found in the tuple")


search_in_tuple([20,15,10,30],10)
search_in_tuple([20,15,10,30],70)
