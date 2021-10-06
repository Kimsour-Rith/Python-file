def find_num(n):
    non_numbers=[]
    if n.isdigit():
        num = int(n)
        print(num*10)
    else:
        for i in n:
            if i not in string.digits:
                   non_numbers.append(i)
        print("The following are not numbers and can't be convered...", non_numbers)

find_num("10abc")
