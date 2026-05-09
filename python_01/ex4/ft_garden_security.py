class Plant:
    def __init__(self, name: str, age: int, height: float) -> None:
        self.name = name
        self._age = 0.0
        self._height = 0.0
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
        else:
            self._height = round(height, 1)
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
        else:
            self._age = age
        print("Plant created: ", end="")
        self.show()

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def set_height(self, height_set) -> None:
        if height_set < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = round(height_set, 1)
            print(f"Height updated: {int(height_set)}cm")

    def set_age(self, age_set) -> None:
        if age_set < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = round(age_set, 1)
            print(f"Age updated: {int(age_set)} days")


def main():
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 20)
    print("\n")
    rose.set_height(25)
    rose.set_age(30)
    print("\n")
    rose.set_height(-12)
    rose.set_age(-1)
    print("Current state: ", end="")
    rose.show()


main()
