inp=input("Enter a number:")
msg="Hello World!"
if len(inp)<1:
    pass
else:
    if inp.isdigit():
        for i in range(int(inp)):
            print(msg)
