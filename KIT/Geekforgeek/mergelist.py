
def merge(lis):
    return [list(ele) for ele in list(zip(*lis))]
lis=[["x","y","z"],["a","b","c"],["Kimsour","Jenny","Jonh"]]
print(merge(lis))
