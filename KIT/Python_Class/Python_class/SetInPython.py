# mySet = {50,65,78,95,25,50}
# mySet2 = {150,655,78,95,75,50}

# print(dir(mySet))
# print(mySet)
# mySet.add(96)
# mySet.remove(78)
# mySet.discard(78)
# help(mySet.discard)
# print(mySet)

#**********************
googleAccHolders = {"Somphors", "Kimhour", "Sothea", "Sovann", "Kimsour"}
fbAccHolders = {"Vatana", "Kimhour", "Sothea", "Ratana", "Hinayo", "Ryuto"}
msAccHolders = {"Ryuto", "Kimhour", "Piseth", "Ratana", "Hinayo"}

print("Students having account in google, FB and MS: ")
print(googleAccHolders.intersection(fbAccHolders).intersection(msAccHolders))

print("Students having account either in google, FB and MS: ")
print(googleAccHolders.union(fbAccHolders).union(msAccHolders))

print(googleAccHolders.difference(fbAccHolders))

