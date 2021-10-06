def name_n_time(name,num_of_time,n=1):
    print(n,name)
    if n<num_of_time:
        name_n_time(name,num_of_time,n+1)
        if n==0:
            return[]


name_n_time("Sereyvath",1)



