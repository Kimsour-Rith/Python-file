msg = "Hello Worldwelcometo KIT"

print(msg)
print(msg[0])
print(msg[-1])
print(msg[2::3])

lastIndex = len(msg)-1
midPoint = len(msg)//2 # 13.0 => Float value (Can't be used in indexes)

rightMid = midPoint + midPoint//2
leftMid =  midPoint//2

print(msg[lastIndex])

print(f"The middle element of your string is {msg[midPoint]}")
print(f"The right mid point {msg[rightMid]}")
print(f"The left mid point {msg[leftMid]}")

print('***************************************')
# String slicing means extracting a particular portion of a String

print(msg[5:]) # Extracts the whole String from 5th Index
print(msg[0:10]) # Prints the first 10 characters from the String
print(msg[0:midPoint+1]) # Prints the first half of the String excluding the mid point
print(msg[midPoint:])

print("######################")

my_list = [20, 50,5,7,9,54,6]
names = ["Vignesh", "Dinesh", "Leo"]

my_list.append(100)
print(my_list)
my_list.insert(5,300)
print(my_list)
my_list.remove(20)
print(my_list)

my_list.pop(3)
print(my_list)

del_value = my_list.pop()
print(my_list)
print(f"The value deleted is :{del_value}")

del my_list[1:3]
print(my_list)

my_list.extend([50,60,50,30])
print(my_list)

