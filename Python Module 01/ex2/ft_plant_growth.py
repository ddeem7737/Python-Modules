class Plant:
    def __init__(self, name: str, age_info: int, height_info: float) -> None:
        self.name = name
        self.age_info = age_info
        self.height_info = height_info

    def show(self) -> None:
        print(f"{self.name}: {self.height_info}cm, {self.age_info} days old")

    def grow(self) -> None:
        self.height_info += 0.8
        self.height_info = round(self.height_info, 1)

    def age(self) -> None:
        self.age_info += 1


def main():
    rose = Plant("Rose", 30, 25)
    print("=== Garden Plant Registry ===")
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.show()
        rose.grow()
        rose.age()


main()
