def linear_search(list,num):
    i=0
    while i<len(list):
        if num in list:
            result=list.index(num)
            print("Number found at",result)
            return result
        else:
            print("Number not found in the list")
            break


linear_search([20,45,65,55,23], 23)
