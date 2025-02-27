class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        return f"{self.name} is chowing down on some grub."

    def sleep(self):
        return f"{self.name} is snoring away after a long day."


class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.milk_produced = 0

    def produce_milk(self):
        self.milk_produced += 5  # Liters, let’s say
        return f"{self.name} produced {self.milk_produced} liters of milk today."


class Chicken(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.eggs_laid = 0

    def lay_egg(self):
        self.eggs_laid += 1
        return f"{self.name} popped out egg #{self.eggs_laid}—fresh from the coop!"


class Pig(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.mud_level = 0

    def roll_in_mud(self):
        self.mud_level += 10  # Arbitrary muddiness scale
        return f"{self.name} rolled in the mud, now at {self.mud_level}% filthy."


# Test the farm
def run_farm():
    bessie = Cow("Bessie", 4)
    clucky = Chicken("Clucky", 2)
    porky = Pig("Porky", 3)

    # Show off the animals and their tricks
    print(f"Farm Animals:")
    print(f"- {bessie.name}, {bessie.age} years old")
    print(f"- {clucky.name}, {clucky.age} years old")
    print(f"- {porky.name}, {porky.age} years old")
    print("\nDaily Routine:")
    print(bessie.eat())
    print(bessie.produce_milk())
    print(clucky.sleep())
    print(clucky.lay_egg())
    print(porky.eat())
    print(porky.roll_in_mud())


# Fire it up
if __name__ == "__main__":
    run_farm()