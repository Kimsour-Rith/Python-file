#Exercise 1: Given two integer numbers return their product.
# If the product is greater than 1000, then return their sum
def multiplication_or_sum(num1,num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

result = multiplication_or_sum(20,30)
print("The result is", result)
result= multiplication_or_sum(30,40)
print("The result is", result)
print("_"*50)
#Exercise 2: Given a range of the first 10 numbers,Iterate from the start number to the end number,
# and In each iteration print the sum of the current number and previous number

def sumNum(num):
    previousNum = 0
    for i in range(num):
        sum = previousNum + i
        print("Current Number", i, "Previous Number ", previousNum," Sum: ", sum)
        previousNum = i

print("Printing current and previous number sum in a given range(10)")
sumNum(10)
print("-"*50)

#Exercise 3: Given a string, display only those characters
# which are present at an even index number.


def printEveIndexChar(str):
  for i in range(0, len(str)-1, 2):
    print("index[",i,"]", str[i])

inputStr = "pynative"
print("Orginal String is ", inputStr)

print("Printing only even index chars")
printEveIndexChar(inputStr)
print("_"*50)
def printOddIndexChar(str):
    for i in range(1, len(str)+2,2):
        print("index[",i,"]", str[i])
inputStr = "pynative"
print("Original String is", inputStr)

print("Printing only odd index chars")
printOddIndexChar(inputStr)
print("_"*50)

