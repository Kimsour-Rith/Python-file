import string


def int_list(lists):
    if lists == []:
        return False
    else:
        for i in range(len(lists)):
            if all(isinstance(item, int) for item in lists):
                return True
            elif all(isinstance(item, str) for item in lists):
                return False
            else:
                return False


print(int_list([]))
print(int_list([1,2,3]))
print(int_list([1,5,2,2,2.0]))
print(int_list([100,200,300,400,500]))
print(int_list(['100','200','300']))
