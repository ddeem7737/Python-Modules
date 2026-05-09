class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._age = age
        self._height = height
        print("Created: ", end="")

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def grow(self) -> None:
        self._height += 0.8
        self._height = round(self._height, 1)

    def age(self) -> None:
        self._age += 1


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self._bloomed = False

    def bloom(self):
        self._bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self._bloomed is True:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(
            f"Tree {self.name} now produces a shade of {self._height}cm long"
            f"and {self.trunk_diameter}cm wide"
            )

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self):
        super().grow()
        self.nutritional_value += 1

    def age(self):
        super().age()
        self.nutritional_value += 1

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutrition value: {self.nutritional_value}")


def main():
    print("=== Grand Plant Types ===\n")

    print("=== Flower")
    rose = Flower("Rose", 15, 10, "Red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("")

    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5.0)
    oak.show()
    print("[asking the oak to produces shade]")
    oak.produce_shade()
    print("")

    print("=== Vegitable")
    tomato = Vegetable("Tomato", 5, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    main()
