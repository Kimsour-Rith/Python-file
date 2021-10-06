# class Car:
#     color = "White"
#     wheel_no = 4
#     max_speed = 120
#
#     def display_detail(self):
#         print(Car.color)
#         print(Car.wheel_no)
#         print(Car.max_speed)
#
# car1 = Car()
# car2 = Car()
#
# car1.display_detail()
# car2.display_detail()
#
# print("#"*20)
# Car.color = "Red"
# Car.wheel_no = 6
# car1.display_detail()
# car2.display_detail()


class Student:
    school_name = "KIT"
    school_location = "Kampong Speu"
    counter = 0

    def __init__(self):
        Student.counter+=1
        print(Student.counter, "Object Created Constructor invoked")

    def display(self):
        print()

    def __del__(self):# Destructor invokes automatically whenever an object is destroyed
        print("Object destroyed")

monirith = Student()
somphors = Student()
rotha = Student()
kimpor = Student()

print("*"*20)
monirith.display()
somphors.display()
rotha.display()
kimpor.display()

# Gabage collector in Python