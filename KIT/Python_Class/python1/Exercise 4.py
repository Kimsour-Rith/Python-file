#Exercise 4: Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string
def removeChars(str, n):
  return str[n:]

print("Removing n number of chars")
print(removeChars("pynative", 5))
print("_"*50)

#Exercise 5: Given a list of numbers, return True if first and last number of a list is same
def isFirst_And_Last_Same(numberList):
    print("Given list is ", numberList)
    firstElement = numberList[0]
    lastElement = numberList[-1]
    if (firstElement == lastElement):
        return True
    else:
        return False

numList = [10, 20, 30, 40, 10]
print("result is", isFirst_And_Last_Same(numList))
numList= [10,20,30,40,55]
print("result is", isFirst_And_Last_Same(numList))
print("_"*50)

#Exercise 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5
