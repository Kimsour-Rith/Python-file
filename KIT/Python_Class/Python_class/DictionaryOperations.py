# myNewDictionary = dict(somphors=87977, piseth=879742, Kimhour=8742211)

userNameList = ['somphors','piseth','Kimhour']
passWordList = [87977,879742,8742211]

mixedValues = zip(userNameList,passWordList)
myNewDict = dict(mixedValues)

print(myNewDict['somphors'])

print(myNewDict.get('Neak',"No such name available in the dictionary"))

myNewDict['Neak'] = 8722121
print(myNewDict.get('Neak',"No such name available in the dictionary"))

