f = None
user = input("Enter file name: ")
try:
    f = open(user,"r")
    read = f.readlines()
    for i in read:
        #print(i)
    print("*"*10)
    for j in read:
        if '#' in j:
            print(j)
except Exception as e:
    print(e)
finally:
    f.close()
    print("File closed successfully")