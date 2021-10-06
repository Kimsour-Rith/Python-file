nameList = ["Sothea", "Sovann", "kettesak", "Piseth"]
print(nameList)
for i in nameList:
    print(i)

user_nameAndPassword={"Sothea":123, "Sovann":234, "kettesak":12, "Piseth":986}
#print(use_nameAndPassword.key())
#print(use_nameAndPassword.value())
print("_"*50)
for key in user_nameAndPassword:
    print(user_nameAndPassword[key])
for value in user_nameAndPassword:
    print(user_nameAndPassword[value])
