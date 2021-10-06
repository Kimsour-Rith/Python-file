# Write a Python function to check whether a number is perfect or not
def perfect_number(num):
    sum = 0
    for x in range(1,num):
        if num % x == 0:
            sum += x            # 1+2+3 = 6
    if sum == num:              # 6 = 6
        print(num," is a perfect number")
    else:
        print(num, " is not a perfect number")


perfect_number(6)


def perfect(num):
    divisors = []
    if num > 0:
        for i in range(1, num):
            if num%i == 0:
                divisors.append(i)
    if sum(divisors) == num:
        return print("Perfect")
    return print("Imperfect")