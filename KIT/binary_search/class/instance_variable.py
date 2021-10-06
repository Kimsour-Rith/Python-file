class Student:
    school = "KIT"
    country = "Cambodia"  # created in class but outside the method
    dorm = "Borey R"

    def __init__(self,s_id,s_name,s_age):           # parameter construtor.
        # is used to create instance variable
        self.s_id = s_id
        self.s_name = s_name
        self.s_age = s_age
        print("Object initialized")

    def display_value(self):
        print(self.s_id)
        print(self.s_name)
        print(self.s_age)       # is called instant method. the method that created in class
        print(Student.school)      # but inside the method
        print(Student.country)
        print(Student.dorm)


kimsour= Student(12,"Kimsour",20)
sreylin = Student(13, "Sreylin",18)

kimsour.display_value()
sreylin.display_value()
