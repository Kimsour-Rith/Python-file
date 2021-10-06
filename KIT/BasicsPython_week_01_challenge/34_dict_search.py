# import itertools
# original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
# new_merged_list = list(itertools.chain(*original_list))
# print(new_merged_list)

def dict_search(info):
    info_students = {"username": "sabbe_k", "score": 100, "comments": "Good job!"}
    for key,value in info_students.items():
        if info == key:
            return "\""+ str(value)+ "\""
        elif info not in info_students:
            return f'"ERROR: {info} not found."'


print(dict_search("username"))      #"sabbe_k"
print(dict_search("score"))         #100
print(dict_search("comments"))      #"Good job!"
print(dict_search("email"))         #"ERROR: 'email' key not found."
print(dict_search("phone_number"))  #"ERROR: 'phone_number' key not found."
