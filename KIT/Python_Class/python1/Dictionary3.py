userNameAndPw = { 'somphors': 123, 'kimsour':456, 'sother':789}

userName = ['somphors','kimsour','sothea']
password = ( 123,456,789)

mixValues = zip(userName,password)
myNewDict = dict(mixValues)
print(myNewDict)
myNewDict['Leakhena'] = 4724
print(myNewDict)
print(myNewDict.get('Leakhena'))

mixValues = zip(userName,password)
myNewSet = set(mixValues)
print(myNewSet)

mixValues = zip(userName,password)
myNewList = list(mixValues)
print(myNewList)

mixValues = zip(userName,password)
myNewTuple = tuple(mixValues)
print(myNewTuple)

userName = ['rith','kim','sour']
password = [324,176,577]
mixValues = zip(userName,password)
myNewTuple = tuple(mixValues)
print(myNewTuple)

