
import json

#Deserialize => Reading from a Json file into Python(Dictionary)/Java(Map)/Php etc objects
with open("employee_data.json","r") as fp:
    my_dict = json.load(fp)

    print(my_dict)

    for employee in my_dict['employees']:
       del employee['age']

    print(my_dict)
    fp.close()

with open("employee_data1.json","w") as fp:
    json.dump(my_dict, fp,indent=2, sort_keys=True)

# {
#                     "employees":[
#                         {
#                             "name":"Dinesh",
#                             "age":30,
#                             "country":"India",
#                             "company":"KIT"
#                         },
#                         {
#                             "name":"Vignesh",
#                             "age":30,
#                             "country":"India",
#                             "company":"KIT"
#                         },
#                         {
#                             "name":"Chester",
#                             "age":40,
#                             "country":"Philipnes",
#                             "company":"KIT"
#                         }
#                     ]
#                 }
