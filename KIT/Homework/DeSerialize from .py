import json

#Deserialize => Reading from a Json file into Python(Dictionary)/Java(Map)/Php etc objects
with open("customers_data.json","r") as fp:
    my_dict = json.load(fp)

    print(my_dict)
    for employee in my_dict['customer']:
        print(employee["name"])
