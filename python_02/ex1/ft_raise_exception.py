def input_temperature(value):
    temp = int(value)
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")

    return temp


def test_temperature():
    print("=== Garden Temperature Checker ===")
    tests = ["25", "abc", "100", "-50"]

    for t in tests:
        print(f"Input data is '{t}'")
        try:
            temp = input_temperature(t)
            print(f"Temperature is now {temp}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")

    print("All tests are complete!!")


if __name__ == "__main__":
    test_temperature()
