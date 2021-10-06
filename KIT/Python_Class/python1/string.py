msg = "hello world welcome to KIT"
print(msg)
print(len(msg)) # len is used to count the amount of string
print(msg[0])
print(len(msg)//2) # // is used to get the integer number.  / is used to get the decimal number
# o index mean the location of letter h, it is counted from 0,1,2,3... and if you want to reverse counting you have to start with -1,-2,-3...
print("_"*50)
print(msg[-1])  # it show the last index
LastIndex = len(msg)-1 # It will show number 25 location
midpoint = len(msg)//2 # 13.0 => Float value ( can't be used in indexes)
print(len(msg)//2)
rightMid = midpoint + midpoint//2 # This mean the middle element of the right string
leftMid = midpoint - midpoint//2 # This mean the middle element of the left string
print(msg[LastIndex]) # print(msg[lastIndex] = print(msg[-1])

print("_"*50)
print(midpoint) # It show the number location of string
print(rightMid)  #It show the number location of string
print(leftMid) #It show the number location of string

print("_"*50)
print(msg[midpoint]) # show the specific string
print(msg[rightMid]) # show the specific string
print(msg[leftMid])  # show the specific string

print("_"*50)
print(f"The middle element of your string is {msg[midpoint]}")
print(f"The right mid point is {msg[rightMid]}")
print(f"The left mid point is {msg[leftMid]}")

print("*****************")
# String slicing means extracting a particular partion of a String
print(msg[:2])
