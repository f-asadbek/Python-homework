class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}!")

    def sleep(self):
        print(f"{self.name} is sleeping...")


class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Moo")

    def produce_milk(self):
        print(f"{self.name} is producing milk.")


class Chicken(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Cluck")

    def lay_egg(self):
        print(f"{self.name} laid an egg!")


class Sheep(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Baa")

    def shear(self):
        print(f"{self.name} is being sheared for wool.")


# Example Usage
cow = Cow("Cowy", 5)
chicken = Chicken("Chicken", 2)
sheep = Sheep("Wooly", 4)

cow.make_sound()
cow.produce_milk()
cow.sleep()

chicken.make_sound()
chicken.lay_egg()
chicken.sleep()

sheep.make_sound()
sheep.shear()
sheep.sleep()
