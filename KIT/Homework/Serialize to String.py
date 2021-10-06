# Serialize to String
import json
my_json_data = '''
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
my_dict = json.loads(my_json_data)        # convert from json data to dictionary,convert pi string used json.loads, if convert pi file used json.load
print(type(my_json_data))
print(type(my_dict))
print(my_dict['employee'][0])
# for employee in my_dict['employees']:
#    del employee['country']

my_json_data = json.dumps(my_dict, indent=2, sort_keys=True)      # change from python dictionary to json
print(my_dict)                                                                                       json
print(my_json_data)
print(type(my_json_data))
print(type(my_dict))