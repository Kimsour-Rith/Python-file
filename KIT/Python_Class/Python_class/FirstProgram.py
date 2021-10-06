a = 10
name = 'Rotha'
place = 'Kampong Cham'
character = 'Is a smart girl'
filePath = r"c:\users\vignesh\newfolder" # \n => New line \u => Underscore \b => Bold => r stands for raw(Un processed) String

print(name+character+' and she is from '+place)
print("Rotha"'Kampong Cham') # Hard coded String not recommended

hi = "Cambodia is well-known for \"Ankorwat\", and it's a great temple"
print("{} {} {}".format(name,character,place))

print(name+name+name) # Concatenates and Prints the name for 3 times
print((name+'\n')*100) # Prints Rotha for 100 times each time with a new line

print(filePath)
