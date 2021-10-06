def dict_values(dicts):
    values=[data for data in dicts.items()]
    mynewdict=dict(values)
    print(mynewdict)
    for key, value in mynewdict.items():
        remove_sign=" ".join(dicts[key])
        print(key,":",remove_sign,"\n*****")


dict_values({120:("Visal","Borey","Sovann"),130:("Hout","Mouyleng","Pidor"),140:("Nary","Misora","Masaaki")})
