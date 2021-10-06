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

class Cow(Animal):      # child/sub/derived
    pass
animal1 = Animal(124,100,"Black",30)
animal2 = Animal(130,150, "Brown", 40)

animal1.display()
animal2.display()