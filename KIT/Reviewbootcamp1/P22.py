def fun_split(string):
    if len(string)<1:
        return []
    else:
        return list(string.split())

print(fun_split("Hello world welcome to Python"))
print(fun_split(''))
