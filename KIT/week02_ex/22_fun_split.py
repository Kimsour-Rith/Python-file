def fun_split(lst):
    if len(lst)<1:
        return []
    else:
        return list(lst.split())
print(fun_split("Hello world welcome to Python"))
print(fun_split(""))

