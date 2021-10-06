def mean_of_list(*args):
    sum_num = 0
    for i in args:
        sum_num += i
    avg = sum_num / len(args)
    return avg

print(mean_of_list(50,10,62,32))
