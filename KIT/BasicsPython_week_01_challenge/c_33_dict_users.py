def dict_users(strings):
    if strings == []:
        return []
    else:
        list = []
        for i in range(0,len(strings)):
            key = ['username','ID']
            mix = dict(zip(key,[strings[i],i+1]))
            list.append(mix)
        return list


print(dict_users(["Akai", "Roger", "Fanny", "Diggie"]))
print(dict_users([]))
