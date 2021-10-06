import json
with open("employee_data.json","r") as fp:  #fp stand for file pointer
    my_dict = json.load(fp)                 # Read from json file in the form of python
    print(my_dict)                          # And this is called DeSerializing


    for i in my_dict["employee"]:
        del i["Age"]
    print(i)
    fp.close()

with open("employee_data.json","w") as fp:
    json.dump(my_dict,fp, indent=2, sort_keys= True)
