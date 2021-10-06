a= int(input("Enter a number:"))
b= int(input("Enter another number:"))
if a>0 and b>0:
    c=a/b
    print("Result:",c)
else:
    try:
        c=a//b
    except:
        print("Divided zero issue, your input is wrong")
    print("Success")

# a= int(input("Enter a number:"))
# b= int(input("Enter another number:"))
#
# print("Input successful")
# try:
#     print("Before the probematic code")
#     c=a/b
#     print("After the probematic code")
# except Exception as d:
#     print("The error is :",d)
# else:
#     print("No exception")
# print("Success")



# try:
#     a= int(input("Enter a number:"))
#     b= int(input("Enter another number:"))
#     c=a/b
#     print("Input successful")
# except Exception as d:
#     print("The error is :",d)
# else:
#     print("No exception")
# finally:
#     print("Don't worry")


print("You are trying to open the file")
try:
    file=open("file1.txt","r")
    print("Reading from the file")
except IOError as error:
    print("Unable to work with the file", error)
finally: # We use finally to release / close the resources
    print("File closed Successully")

print("Success...")

