def initials(lists):
    if lists == []:
        return []
    else:
        my_list=[]
        for i in lists:
            f_char = i[0]
            my_list.append(f_char.upper())
        return my_list


print(initials(['World', 'Wide', 'Web']))                 #['W', 'W', 'W']
print(initials(['South', 'East', 'Asia']))                    #['S', 'E', 'A']
print(initials(['Good', 'luck', 'have', 'fun']))             #['G', 'L', 'H', 'F']
print(initials([]))          #[]
