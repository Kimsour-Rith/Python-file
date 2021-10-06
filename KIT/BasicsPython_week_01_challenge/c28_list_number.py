def list_number(start,end,reverse=False):
    if reverse == True:
        return list(reversed(range(start,end+1)))
    elif reverse == False:
        return list(range(start,end+1))
    else:
        return list(range(start,end+1))


print(list_number(1,10))
print(list_number(1,10,reverse=True))
print(list_number(1,10,reverse=False))
print(list_number(20,25))
print(list_number(20,25,reverse=True))
