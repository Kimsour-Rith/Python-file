from collections import Counter
def dict_count(lists):
    new_list =[]
    for i in lists:
        st = str(i)
        new_list.append(st)
    res = Counter(new_list)
    return dict(res)



print(dict_count([1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5]))    #{"1": 4, "2": 3, "3": 2, "4": 2, "5": 1}
print(dict_count(["hey", "hi", "hi", "hi"]) )              #{"hey": 1, "hi": 3}
print(dict_count(["python", "python", "c++"]))              #{"python": 2, "c++": 1}
print(dict_count(["a", "b", "c", "d", "e"]))                #{"a": 1, "b": 1, "c": 1, "d": 1, "e": 1}
print(dict_count([]))                                       #{}