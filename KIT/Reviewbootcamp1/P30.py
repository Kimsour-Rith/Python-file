def dict_values(dicts):
    set1=[item for item in dicts]
    key1=[num for num in item]
    tuple1=[mytup for mytup in item]
    string=tuple([name for name in mytup])
    mixvalue=zip(key1,string)
    mixdict=dict(mixvalue)
