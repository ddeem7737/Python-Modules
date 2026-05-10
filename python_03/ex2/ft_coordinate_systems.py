import math


def get_player_pos() -> tuple:
    raw = input("Enter new coordinates as floats 'x,y,z': ").split(',')

    if len(raw) != 3:
        print("Invalid syntax")
        return get_player_pos()

    coords = []
    for val in raw:
        try:
            coords.append(float(val.strip()))
        except ValueError:
            print("Invalid syntax")
            return get_player_pos()
    return tuple(coords)


def distance_calc(pos1: tuple, pos2: tuple) -> float:
    return math.sqrt((pos1[0] - pos2[0])**2 +
                     (pos1[1] - pos2[1])**2 + (pos1[2] - pos2[2])**2)


def first_text(pos: tuple) -> None:
    print(f"Got a first tuple: {tuple(pos)}")
    print(f"It includes: X={pos[0]}, Y={pos[1]}, Z={pos[2]}")


print("Get a first set of coordinates")
pos1 = get_player_pos()
first_text(pos1)
print(f"Distance to center: {distance_calc(pos1, (0, 0, 0))}")
print("Get a second set of coordinates")
pos2 = get_player_pos()

print(f"Second tuple: {tuple(pos2)}")
print(f"It includes: X={pos2[0]}, Y={pos2[1]}, Z={pos2[2]}")
print(f"Distance to center: {distance_calc(pos2, (0, 0, 0))}")
print(f"Distance between points: {distance_calc(pos1, pos2)}")
