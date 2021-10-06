#Write a python program to read data from a JSON file and also add a new data in the same JSON file

import json

#Deserialize => Reading from a Json file into Python(Dictionary)/Java(Map)/Php etc objects
with open("customers_data.json","r") as f:
    my_dict = json.load(f)

    print(my_dict)
    for customer in my_dict['customer']:
        print(customer["name"])



# import json
# json_data ='''
#                 {
#                     "customers":[
#                         {
#                             "name":"Kimsour",
#                             "age":20,
#                             "country":"Cambodia",
#                             "company":"Pizza"
#                         },
#                         {
#                             "name":"Sreylin",
#                             "age":18,
#                             "country":"America",
#                             "company":"KOI"
#                         },
#                         {
#                             "name":"Somphors",
#                             "age":20,
#                             "country":"Cambodia",
#                             "company":"Amazon"
#                         }
#                     ]
#                 }
#             '''
#
# dict = json.loads(json_data)      # store jea python dictionary
# print(type(json_data))
# print(type(dict))
#
# print(dict["employees"][0])
#
# for item in dict["employees"]:
#     del item["age"]
#
# print(dict)
