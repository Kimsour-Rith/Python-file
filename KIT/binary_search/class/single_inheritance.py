class Customer:
    def __init__(self, id, name, age, height):
        self.id = id
        self.name = name
        self.age = age
        self.height = height

    def display(self):
        print(self.id)
        print(self.name)
        print(self.age)
        print(self.height)
        print("Parent Class")
class Lady(Customer):
    def display_lady(self):
        print(self.id)
        print(self.name)
        print(self.age)
        print(self.height)
        print("Student Class")

cus1 = Lady(12,"Kimsour",20,160)
cus2 = Lady(13,"Lin",17,160)

cus1.display_lady()
print("*"*10)
cus2.display_lady()


