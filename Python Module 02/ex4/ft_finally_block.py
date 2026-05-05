class GardenError(Exception):
    def __init__(self, name="Unkown Garden Error"):
        super().__init__(name)


class PlantError(GardenError):
    def __init__(self, name="Unkown Garden Error"):
        super().__init__(name)


def water_plant(plant_name):
    if plant_name == plant_name.capitilize():
        raise PlantError(f"Invalid plant name to water: {plant_name}")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system():
    print("=== Garden Watering System ===")

    print("Testing Valid Plants")
    try:
        print("Opening Watering System")

        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print("... ending test and returning to main")
        return
    finally:
        print("Closing watering system")

    print("Testing invalid plants...")

    try:
        print("Opening Watering System")

        water_plant("Tomato")
        water_plant("lettuce")

    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print("... ending tests and returning to main")
        return
    finally:
        print("Closing Watering system")

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
