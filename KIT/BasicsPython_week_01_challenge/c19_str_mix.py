inp=input("Enter a word:")
if inp.upper():
    if len(inp)==1:
        print(inp*4)
    elif len(inp)=="":
        print("0"*4)
    elif len(inp)==2:
        print(inp*2)
    else:
        name1=inp[0:2]   # or you also can write name1=inp[0:2][::-1]
        n1=name1[::-1]   # or you also can write name2=inp[-2:][::-1]
        name2=inp[-2:]
        n2=name2[::-1]
        print(n1+n2)
