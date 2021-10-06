import string
def sum_num(mystr):
    sum=0
    for i in mystr:
        if i.isdigit():
            num = int(i)
            sum+=num
    print("Sum of number in string =",sum)

    for i in mystr:
        if i not in string.digits:
            pass


sum_num("123Kimsour")


