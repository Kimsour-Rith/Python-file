myset = {10,20,30,40,50,60,70,80}
myset2 ={12,25,30,70,454,80}
myset3 ={35,90,60,12,70,80,25,67}
print(dir(myset))
print(myset.intersection(myset2).intersection(myset3))
print(myset.union(myset2).union(myset3))
print(myset.difference(myset2))
print(myset.difference(myset2).difference(myset3))
print(myset.difference(myset2.difference(myset3)))
print("_"*50)
google = { "cat","dog","bird","frog"}
fb = {"bird", "chicken","ant","kite","rabbit","dog"}
ms = {"crocodile","snack","cat","frog","bird"}
print(google.intersection(fb).intersection(ms))
print(google.union(fb).union(ms))
print(google.difference(fb).difference(ms))
