user_inp=[]
while True:
    inp=input("Enter a sentence:")
    if inp!="GENERATE":
        user_inp.append(inp)
    elif inp=="GENERATE":
        if user_inp==[]:
            print("Nothing to display")
            break
        else:
            for i in user_inp:
                print(f'<p>{i}</p>')
            break
