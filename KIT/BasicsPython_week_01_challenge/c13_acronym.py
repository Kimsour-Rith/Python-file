inp=input("Enter a sentence:")
if "OOP" or "FP" or "AI" in inp:
    print(inp.replace("OOP","Object Oriented Programming").replace("FP","Functional Programming").replace("AI","Artificial Intelligence"))
else:
    print(inp)

