class Animal:       # Parent/ Base/ Super Class
    def __init__(self,weight,height,color,speed):
        self.weight = weight
        self.height = height
        self.color = color
        self.speed = speed
    def display(self):
        print(self.weight)
        print(self.height)
        print(self.color)
        print(self.speed)
        print("I am an animal")
class Dog(Animal):
    def display(self):
        super().display()       # Animal.display(self)
        print("I am a Dog")
class Rabit(Dog):
    def display(self):
        super().display()   # or you can say   Dog.display(self)
        print("I am a Rabit")


rabit = Rabit(45,100, "Gray",140)
rabit.display()