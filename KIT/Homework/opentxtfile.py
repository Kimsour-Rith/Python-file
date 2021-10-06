file1 = None
file2 = None
try:
    file1 = open("C:/Users/user/Desktop/test1.txt","w")
    text = input("You can input some text...")+"\n"
    file1.write(text)

    file1 = open("C:/Users/user/Desktop/test1.txt","r")
    text2 = file1.read()

    file2 = open("C:/Users/user/Desktop/test2.txt","r+")
    user_input = int(input("Input position of file pointer: "))
    file2.seek(user_input)
    file2.write(text2)

except Exception as e:
    print("Unable to open the file",e)
finally:
    file1.close()
    file2.close()
    print("File closed successfully")

