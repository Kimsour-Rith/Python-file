from collections import Counter
while True:
    paragraph= input("Please input a paragraph:\n")
    search= input("Please input a search string:\n")
    if search in paragraph:
        counter= Counter(paragraph)
        print("There are",counter[search],"Occurrences\n")
        yn = input("Do you want to replace the text ?[Y/N]\n")
        if yn == "Y" or yn =="y" :
            input1=input("Please input a replacement string:\n")
            print(counter[search],"Words has been replaced from the paragraph")
            print(paragraph.replace(search,input1))
            pass
        elif yn == "N" or yn=="n":
            respond=input("Oh you don't like to replace, Do you want to check it again[Y/N]?\n")
            if respond=="Y":
                pass
            elif respond=="N":
                break
            else:
                print("Invalid input")
                pass


        else:
            print("Please give proper input")
            continue

