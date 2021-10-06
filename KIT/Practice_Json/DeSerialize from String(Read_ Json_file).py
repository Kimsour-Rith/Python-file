#create json
#Covert Json to Python/ Java/ PHP object is called DeSerializing or Decoding
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
print("*"*100)
print(my_dict)
print(type(my_dict))
print("*"*100)
print(my_dict["employee"])      # print all the value of the key employee
print("*"*100)
print(my_dict["employee"][0])
print("*"*100)
print(my_dict["employee"][1])
print("*"*100)
print(my_dict["employee"][2])
print("#"*100)
# for person in my_dict["employee"]:  # used to iterate every element in dictionary
#     print(person)
    # print(person["Name"])
    # print(person["Age"])
    # print(person["Company"])

for i in my_dict["employee"]:
    del i["Age"]
    #del i["Company"]
    #del i["Name"]
print(my_dict)
