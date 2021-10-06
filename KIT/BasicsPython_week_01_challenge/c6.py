def print_n_time(name,n):
    print(name,n)
    if n==0:
        return
    for i in reversed(range(1,n)):
        print_n_time (name,i)


print_n_time("Kimsour",10)
