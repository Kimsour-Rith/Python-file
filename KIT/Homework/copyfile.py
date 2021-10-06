
try:
    file1 = open("C:/Users/user/Desktop/test1.txt","r")
    text2 = file1.read()

    file1 = open("C:/Users/user/Desktop/test1.txt","r")
    text2 = file1.read()

    file2 = open("C:/Users/user/Desktop/test2.txt","w")
    file2.write(text2)


except:
    print("Unable to open the file")
finally:
    file1.close()
    file2.close()
    print("File closed successfully")

