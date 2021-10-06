def odd_even_list(lists):
    if lists==[]:
        return []
    else:
        res=['EVEN'if i%2==0 else 'ODD' for i in lists]
        return res

print(odd_even_list([]))
print(odd_even_list([1,22,111,444]))
print(odd_even_list([2,11,222,333]))
print(odd_even_list([1,2,3,4,555]))
