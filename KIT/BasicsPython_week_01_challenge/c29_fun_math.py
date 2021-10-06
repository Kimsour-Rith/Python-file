def fun_add(num1,num2):
    return num1+num2

def fun_sub(num1,num2):
    return num1-num2

def fun_mul(num1,num2):
    return num1*num2

def fun_div(num1,num2):
    if num1<num2:
        return num1/num2
    else:
        return num1//num2
print(fun_add(-1,1001))
print(fun_add(1.5,1.5))
print("*"*10)
print(fun_sub(-1,1001))
print(fun_sub(1.5,1.5))
print("*"*10)
print(fun_mul(4,22))
print(fun_mul(1.5,1.5))
print("*"*10)


print(fun_div(1,10))
print(fun_div(25,5))
