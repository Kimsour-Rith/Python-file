#create json
# Make change or rewrite in Json file is called Serializing/ Encoding
import json
my_json_data = '''
                {
                    "employee":[
                        {
                            "Name": "Jenny",
                            "Age" : 23,
                            "Company" : "Blackpink"
                        },
                        {
                            "Name" : "Lisa",
                            "Age" : 22,
                            "Company" : "Blackpink"
                        },
                        {
                            "Name" : "Kimsour",
                            "Age" : 20,
                            "Company" : "KIT"
                        }   
                    ] 
                }                

            '''
my_dict = json.loads(my_json_data)  # It is going to convert json to python dictionary, we call this method as deserializing or decoding ( read Json file)
print(my_json_data)
print(type(my_json_data))
print("*"*80)
print(my_dict)
print(type(my_dict))
print("#"*80)
# for i in my_dict["employee"]:
#     #del i["Age"]
#     #del i["Company"]
#     #del i["Name"]
# print(my_dict)
# print("="*80)

my_json_data = json.dumps(my_dict, indent=2,sort_keys = True)     # you reassign it by using (dumps) and dumps is used to write from python to json file (Serializing)
print(my_json_data)
print(my_dict)
