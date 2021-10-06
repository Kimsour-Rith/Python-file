class Student:
    school_name = "KIT"
    school_location = "Kampong Speu"
    counter = 0
    def display(self):
        print(Student.school_name)
        print(Student.school_location)

    def __init__(self): # Constructor are special methods (init) # Constructor To initialize instance variables
        # Constructor called automatically
        # we called it depend number of object creation
        Student.counter += 1
        print(Student.counter, "Object Created Constructor invoked")

    # def display(self):
    #     print("hii")

    def __del__(self):           # Destructor invokes automatically whenever an object is destroyed
        # Destructor is a special method that invoke  when an object is destroyed
        # it destroy after the block of code execute
        # Garbage collector destroy the object
        print("Object destroyed")

class Car:
    color = "Black"
    max_speed = 150
    min_speed = 100
    num_wheels = 4

    def display_details(self):
        print(Car.color)
        print(Car.max_speed)
        print(Car.min_speed)
        print(Car.num_wheels)


car1 = Car()
car2 = Car()

car1.display_details()
car2.display_details()
print("*"*10)

Car.color = "Brown"
car1.display_details()
car2.display_details()

monirith = Student()            # print block __int__(self)
somphors = Student()
rotha = Student()
kimpor = Student()
#
print("*"*10)
monirith.display()
somphors.display()
rotha.display()
kimpor.display()
#print("*"*10)

#Garbage collector in Python