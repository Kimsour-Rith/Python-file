# import json : to convert Python to  json data
# Python => json : Serialige = encode
# json.dumps(name_variable, indent = True)
# import json
# my_json_data = '''
#                 {
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
#             '''
# # print(my_json_data["employees"])   # Error
#                   # Convert string to Dict in Json
# my_dict = json.loads(my_json_data)     # .loads :"s" "String"
# print("="*30,"String","="*30,"\n")###########################
#
# print("Type of my_Json_Data: ",type(my_json_data))
# print("==> String: " ,my_json_data)
#
# print("="*30,"Dictionary","="*30,"\n")#######################
#
# print("Type of my_dict: ", type(my_dict))
# print("==> Dict: ", my_dict)
#
# print("="*30, "Information of employees","="*30,"\n")#######################
#
# print(my_dict["employees"])
#
# print("="*30,"Idexing","="*30,"\n")
#
# print(my_dict["employees"][0])
# print(my_dict["employees"][1])
# print(my_dict["employees"][2])
# print("="*30,"loop","="*30,"\n")
# # use for loop
# for i in my_dict["employees"]:
#    print(i)
#    print("**"*30)
#
# print("="*30,"name, age, country, company","="*30,"\n")#######################
# for em in my_dict['employees']:
#    print(em)
#    print(em['name'])
#    print(em['age'])
#    print(em['country'])
#    print(em['company'])
#    print("="*30)#######################
#
#
# # Convert Dict => Json data(string)
# print("="*30,"Convert python(dict) to Json data(string or text)","="*30,"\n")#######################
# my_new_json = json.dumps(my_dict, indent = True)
# print("New_Json: ", my_new_json)


################## From Json to Python and delete sth then convert to Json
print("="*30,"Delete some information, then store it to json","="*30,"\n")###########################
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
# print(my_json_data["employees"])   # Error
                  # Convert string to Dict in Json
my_dict = json.loads(my_json_data)     # .loads :"s" "String"
print("="*30,"String","="*30,"\n")###########################

print("Type of my_Json_Data: ",type(my_json_data))
print("==> String: " ,my_json_data)

print("="*30,"Dictionary","="*30,"\n")#######################

print("Type of my_dict: ", type(my_dict))
print("==> Dict: ", my_dict)

print("="*30, "Information of employees","="*30,"\n")#######################

print(my_dict["employees"])

print("="*30,"Idexing","="*30,"\n")

print(my_dict["employees"][0])
print(my_dict["employees"][1])
print(my_dict["employees"][2])
print("="*30,"loop","="*30,"\n")
# use for loop
for i in my_dict["employees"]:
   print(i)
   print("**"*30)

print("="*30,"name, age, country, company","="*30,"\n")#######################
for em in my_dict['employees']:
   print(em)
   print(em['name'])
   print(em['age'])
   print(em['country'])
   print(em['company'])
   print("="*30)#######################

print("="*30,"Delete Data", "="*30,"\n")#######################
for j in my_dict["employees"]:
   del j["age"]
   del j["company"]
print(my_dict)       # it delete in Python(dict) file
print(my_json_data)  # it doesn't deletes in Json file


# Convert Dict => Json data(string)
print("="*30,"Convert python(dict) to Json data(string or text)","="*30,"\n")#######################
# my_new_json = json.dumps(my_dict, indent = True)
my_new_json = json.dumps(my_dict)
print("Type of my_new_Json: ", type(my_new_json))    # String
print("my_new_Json is ", type(my_new_json),": ", my_new_json)                  # string


# ############# indent ##################
print("="*30,"Indent = 0", "="*30,"\n")#######################
my_new_json = json.dumps(my_dict, indent = 0)
print(my_new_json)
# indent = 0
print("="*30,"Indent = 1","="*30,"\n")#######################
my_new_json = json.dumps(my_dict, indent = 1)
print(my_new_json)
# indent = 1
print("="*30,"Indent = 1", "="*30,"\n")#######################
my_new_json = json.dumps(my_dict, indent = 1)
print(my_new_json)
# indent = 2
print("="*30,"Indent = 2", "="*30,"\n")#######################
my_new_json = json.dumps(my_dict, indent = 2)
print(my_new_json)
