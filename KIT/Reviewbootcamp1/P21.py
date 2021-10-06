def fun_calc(num1,num2,operator):
    if operator=="+":
        product=num1+num2
        print(f'Product: {product}')
    elif operator=="-":
        product=num1-num2
        print(f'Product:{product}')
    elif operator=="*":
        product=num1*num2
        print(f'Product:{product}')
    elif operator=="/":
        product=num1/num2
        print(f'Product:{product}')
    print(f'Process:{num1}{operator}{num2}={product}')


fun_calc(50,2,"+")
