class Plant:
    def __init__(self, name: str, age_info: int, height_info: float) -> None:
        self.name = name
        self.age_info = age_info
        self.height_info = height_info
        print("Created: ", end="")
        self.show()

    def show(self) -> None:
        print(f"{self.name}: {self.height_info}cm, {self.age_info} days old")

    def grow(self) -> None:
        self.height_info += 0.8
        self.height_info = round(self.height_info, 1)

    def age(self) -> None:
        self.age_info += 1


def main():
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 30, 25)
    sunflower = Plant("Sunflower", 45, 80)
    cactus = Plant("Cactus", 120, 15)
    oak = Plant("Oak", 365, 200)
    fern = Plant("Fern", 120, 12)
    print("=== The Plants Are growing ===")
    rose.grow()
    sunflower.grow()
    cactus.grow()
    oak.grow()
    fern.grow()


main()
