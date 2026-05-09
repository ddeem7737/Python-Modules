class Plant:
    def __init__(self, name: str, age: int, height: int) -> None:
        self.name = name
        self.age = age
        self.height = height

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main():
    rose = Plant("Rose", 30, 25)
    sunflower = Plant("Sunflower", 45, 80)
    cactus = Plant("Cactus", 120, 15)
    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()


main()
