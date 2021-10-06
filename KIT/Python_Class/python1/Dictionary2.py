studentNameAndPw = {'somphors': '1234','kimsour':'5432', 'makara':'431'}
print(studentNameAndPw['somphors'])

newDict = dict(somphors=1234, kimsour=5432, makara=431)
print(newDict)

studentNameAndPw = {'somphors':[12,23,35,67],'kimsour': (54,45,56,44), 'makara': {'google':'google123,'twitter':'tw123','FB':['fb123','fb56','fb78']},}
# print(studentNameAndPw['somphors'][-2])
# print(studentNameAndPw)
print(studentNameAndPw['makara']['FB'][-1])

