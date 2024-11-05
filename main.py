
class Bird:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def fly(self):
        print(self.name, "is flying!")

    def eating(self):
        print(self.name, "is eating!")


class Penguin(Bird):
    def __init__(self, name, color, swimmingspeed):
        super().__init__(name, color)
        self.swimmingspeed = swimmingspeed

    def swim(self):
        print(self.name, "is swimming at", self.swimmingspeed, "km/h!")


penguin = Penguin("Penguin", "Black and White", 10)

penguin.fly()       
penguin.eating()      
penguin.swim()       


print("Name:", penguin.name, "Colour:", penguin.color, "Swimming Speed:", penguin.swimmingspeed, "km/h")
