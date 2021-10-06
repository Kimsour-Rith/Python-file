class Animal:       # Parent/ Base/ Super Class
    def __init__(self,weight,height,color,speed):
        self.weight = weight
        self.height = height
        self.color = color
        self.speed = speed
    def displayAnimal(self):
        print(self.weight)
        print(self.height)
        print(self.color)
        print(self.speed)
        print("I am an animal")

animal =Animal (123,1,"Black",400)
animal.displayAnimal()
class Dog(Animal):
    def displayDog(self):
        print(self.weight)
        print(self.height)
        print(self.color)
        print(self.speed)
        print("I am a Dog")

dog = Dog(45,100, "Gray",140)
dog.displayAnimal()
print("*"*10)
dog.displayDog()

class Rabit(Dog):
    def displayRabit(self):
        print(self.weight)
        print(self.height)
        print(self.color)
        print(self.speed)
        print("I am a Rabbit")

rabit = Rabit(4,0.5,"White",60)
rabit.displayAnimal()
print("*"*10)
rabit.displayDog()
print("*"*10)
rabit.displayRabit()
