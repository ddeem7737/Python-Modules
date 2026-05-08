import sys


inventory = {}

for i in sys.argv[1:]:
    if ":" not in i or i.count(":") != 1:
        print(f"Invalid parameter: {i}")
        continue
    name, quantity = i.split(':')
    if not name or not quantity:
        print(f"Invalid parameter {i}")
        continue
    if name in inventory:
        print(f"Redudant item: {name} - discarding")
        continue
    try:
        inventory[name] = int(quantity)
    except ValueError:
        print(f"Quantity error for {name}: {ValueError}")

print("\n=== Inventory System Analysis ===")

print(f"Got inventory: {inventory}")

items = list(inventory.keys())
print(f"Item list: {inventory}")

total = sum(inventory.values())
print(f"Total quantity of the {len(items)} items: {total}")

for item in inventory.keys():
    perc = round(inventory[item] / total * 100, 1)
    print(f"Item {item} represents {perc}%")

most = items[0]
least = items[0]

for i in inventory.keys():
    if inventory[i] > inventory[most]:
        most = i
    if inventory[i] < inventory[least]:
        least = i

print(f"Item most abundant: {most} with quantity {inventory[most]}")
print(f"Item least abundant: {least} with quantity {inventory[least]}")

inventory.update({'magic_item': 1})
print(f"Updated inventory: {inventory}")
