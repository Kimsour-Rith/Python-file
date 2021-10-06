def fun_cals(num1,num2,operator):
    if operator=="+":
         product= num1+num2
         print(f'Procuct:{product}')
    elif operator=="-":
        product= num1-num2
        print(f'Procuct:{product}')
    elif operator=="*":
        product= num1*num2
        print(f'Procuct:{product}')
    elif operator=="/":
        product= num1/num2
        print(f'Procuct:{product}')
    print(f'Process: {num1}{operator}{num2}={product}')
    return product


fun_cals(50,2,'*')
