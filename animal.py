class Animal:

    sound = "kein Geräusch"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ": " + self.sound)

    def move(self):
        print(self.name + " bewegt sich davon und sagt " + self.sound)


class Dog(Animal):

    sound = "Wuff!"

    def move(self):
        print(self.name + " rennt weg und sagt " + self.sound)


class Cat(Animal):

    sound = "Miau!"

    def move(self):
        print(self.name + " schleicht umher und sagt " + self.sound)


class Fish(Animal):

    sound = "Blubb!"

    def move(self):
        print(self.name + " schwimmt im Kreis und sagt " + self.sound)


d = Dog("Fifi")
d.speak()
d.move()

c = Cat("Bibi")
c.speak()
c.move()

c2 = Cat("Mimi")
c2.speak()
c2.move()

f = Fish("Nemo")
f.speak()
f.move()
