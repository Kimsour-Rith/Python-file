test_list=[11,22,34,55,67,69,53,88,11,13]
print("The original string is:"+str(test_list))
#get the even indincs from test_list
indics=[idx for idx in range(len(test_list)) if test_list[idx]%2==0]
#get the distance between first and last elememt
res= indics[-1]-indics[0]
print("The even span is:"+str(res))
