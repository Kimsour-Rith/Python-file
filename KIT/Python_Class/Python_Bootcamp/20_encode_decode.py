alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
yOrN= ""
while yOrN != "N":
    print("Press 1 to encode")
    print("Press 2 to decode")
    inp= int(input())
    if inp==1:
        str_ing=input("Enter the string to encode:\n")
        num=len(str_ing)
        str_out=''
        for i in range(num):
            c= str_ing[i]
            loc= alphabet.find(c)
            newloc = (loc+13)%26
            str_out+=alphabet[newloc]
        print("The encode text is: "+str_out)
        print ("\nDo you want to continue?[Y/N]")
        user_inp=input(" ")
        if user_inp=="Y":
            continue
    if inp==2:
        str_ing=input("Enter the string to decode:\n")
        num=len(str_ing)
        str_out=''
        for i in range(num):
            c= str_ing[i]
            loc= alphabet.find(c)
            newloc = (loc-13)%26
            str_out+=alphabet[newloc]
        print("The decode text is: "+str_out)
        print ("\n Do you want to continue?[Y/N]")
        user_inp=input(" ")
    if user_inp=="N":
        break








