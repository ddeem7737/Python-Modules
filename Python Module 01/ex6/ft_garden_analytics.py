class Plant:
    class _Stats:
        def __init__(self):
            self._grow = 0
            self._age = 0
            self._show = 0

        def inc_grow(self):
            self._grow += 1

        def inc_age(self):
            self._age += 1

        def inc_show(self):
            self._show += 1

        def display(self):
            print(f"Stats: {self._grow} grow, "
                  f"{self._age} age, {self._show} show")

    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self._age = age
        self._stats = Plant._Stats()

    def grow(self):
        self._height = round(self._height + 0.8, 1)
        self._stats.inc_grow()

    def age(self):
        self._age = self._age + 1
        self._stats.inc_age()

    def show(self):
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def display_stats(self):
        self._stats.display()

    @staticmethod
    def is_older_than_a_year(days):
        return days > 375

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)


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
        if self._bloomed is False:
            print(f"{self.name} is not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds = 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._shade_calls = 0

    def produce_shade(self):
        self._shade_calls += 1
        print(
              f"Tree {self.name} now produces a shade of "
              f"{self._height}cm long and {self.trunk_diameter}cm wide"
              )

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def display_stats(self):
        super().display_stats()
        print(f"{self._shade_calls} shade")


def display_plant_stats(plant):
    print(f"[statistics for {plant.name}]")
    plant.display_stats()


def main():
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print("Is 30 days more than a year? ->", Plant.is_older_than_a_year(30))
    print("Is 400 days more than a year? ->", Plant.is_older_than_a_year(400))

    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    display_plant_stats(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_plant_stats(rose)

    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5.0)
    oak.show()
    display_plant_stats(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    display_plant_stats(sunflower)

    print("=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    display_plant_stats(unknown)


if __name__ == "__main__":
    main()
