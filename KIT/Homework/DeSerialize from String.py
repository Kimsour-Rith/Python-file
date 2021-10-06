# DeSerialize from String
import json
my_json_data ='''
                {
                    "employees":[
                        {
                            "name":"Dinesh",
                            "age":30,
                            "country":"India",
                            "company":"KIT"
                        },
                        {
                            "name":"Vignesh",
                            "age":30,
                            "country":"India",
                            "company":"KIT"
                        },
                        {
                            "name":"Chester",
                            "age":40,
                            "country":"Philipnes",
                            "company":"KIT"
                        }
                    ]
                }
            '''

my_dict = json.loads(my_json_data)      # store jea python dictionary
print(type(my_json_data))
print(type(my_dict))

print(my_dict["employees"][0])

for employee in my_dict["employees"]:
    del employee["age"]

print(my_dict)
