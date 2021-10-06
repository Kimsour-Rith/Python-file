file1 = None
try:
    file1 = open("C:/Users/user/Desktop/kit.txt","w+")
    message = "Hello world! My name is Rith Kimsour and I am 20 years old"
    file1.write(message)
    file1.seek(0)
    f2 = file1.readlines()
    print(f2)


except Exception as e:
    print("Unable to open the file",e)
finally:
    file1.close()
    print("File closed successfully")


