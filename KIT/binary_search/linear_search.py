def linear_search(list, s_no):
    pos = -1
    for i in range(len(list)):
        if s_no == list[i]:
            return i
    return pos

res = linear_search([50,65,123,23,12], 65)
if res == -1:
    print("Number not found in the list")
else:
    print("Number found at ", res)
