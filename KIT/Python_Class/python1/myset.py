myset = {50,60,34,35,54}
print(myset)

print(dir(myset)) # is used to show all the functions in myset
myset.add(32)
print(myset)

myset.remove(60)
print(myset)

myset.discard(60) # discard is used to verify that you really want to remove something, but it somehow similar to remove function
print(myset)

help(myset.remove)
print(myset)
