def dict_info(firstname,lastname, email, phone):
    my_list = ['firstname', 'lastname', 'email', 'phone']
    if firstname == "" and lastname == "" and email == "" and phone == "" :
        return dict(zip(my_list,[firstname,lastname,email,phone]))
    else:
        f_name = firstname[0].upper() + firstname[1:]  # or you can write f_name = firstname[0].capitalize()
        l_name = lastname.upper()
        value = [f_name,l_name,email,phone]
        mix = zip(my_list,value)
        return dict(mix)


print(dict_info("kevin", "sabbe", "sabbe.kev@gmail.com", "+855 16 804 404"))
print(dict_info("", "", "", ""))
print(dict_info("kevin", "sabbe","",""))

print("*"*20)

def dict_info(*dc):
    my_list = ('firstname', 'lastname', 'email', 'phone')
    return dict(zip(my_list, dc))

print(dict_info('kelvin', 'sabbe', 'sabbe.kev@gmail.com', '+855 967827020'))
print(dict_info('', '', '', ''))