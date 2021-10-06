i=0
while i==0:
  enter=input("Please input aparagragh:")
  list_p=enter.split()
  search=input("Please input a search string: ")
  number=0
  for i in list_p:
    if search.upper() in i.upper():
        number+=1

  print(f"There are {number} occurrence")
  print("Do you want to replace the tet[Y/N]?")
  replace=input()
  if replace.upper()=="Y":
    print("Please Input a replacement string: ")
    replacement=input()

    for j in list_p:
        if j.upper() in i.upper():
            list_p==list_p.replace(replacement,search)
    print(f"{number} words has been replaced from the paragraph")
    print(list_p)

  elif replace.upper()=="N":
    print("Oh! you don't like to replace , Do you want to check agian [Y/N]?")
    check=input()
    if check.upper()=="Y":
        pass
    else:
        i=1
  else:
      print("Please give the proper inut")
