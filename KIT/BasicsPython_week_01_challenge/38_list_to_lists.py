def list_to_lists(a):
    if not a:
        return []
    else:
        rev = []
        for i in a:
            rev.append(i[::-1])
            for j in rev:
                if len(rev)==1:
                    return list(rev)
                else:
                    lists = []
                    for k in j:
                        lists.append(k)
                        print(list(lists))

list_to_lists(["Hello"])                          #[['o', 'l', 'l', 'e', 'H']]
list_to_lists(['A', 'a', 'B', 'b'])               #[['A'], ['a'], ['B'], ['b']]
list_to_lists(["hello", "world"])           #[['o', 'l', 'l', 'e', 'h'], ['d', 'l', 'r', 'o', 'w']]
list_to_lists([])                           #[]


