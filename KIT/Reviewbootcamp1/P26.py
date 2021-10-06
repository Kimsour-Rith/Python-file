def search_in_tuple(mytuple,arg):
    tuple1=(tuple(mytuple))
    if arg in tuple1:
        index1=tuple1.index(arg)
        print(f'Element found at Index:{index1}')
        return index1
    else:
        print("Element not found in the tuple")


search_in_tuple((20,15,10,30),10)
search_in_tuple((20,15,10,30),70)
