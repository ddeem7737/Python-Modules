import random


fixed_list = ['Crafting Genius', 'Strategist', 'World Savior',
              'Speed Runner', 'Survivor',
              'Master Explorer', 'Treasure Hunter',
              'Unstoppable', 'First Steps', 'Collector Supreme',
              'Untouchable', 'Sharp Mind', 'Boss Slayer', 'Chaga Chaga',
              'Boom Bam Badum', 'Optimus Prime', 'Demon Slayer']


def gen_achievements() -> set:
    count = random.randint(1, len(fixed_list))
    return set(random.sample(fixed_list, count))


players = {"Alice": gen_achievements(),
           "Bob": gen_achievements(),
           "Gago": gen_achievements(),
           "Ani": gen_achievements(),
           }
set_list = set(fixed_list)

print("=== Achievement Tracker System ===")
print("=== All Achievements ===")
for name, ach in players.items():
    print(f"Player {name}: {ach}")

all_ach: set[str] = set()
for ach in players.values():
    all_ach = all_ach.union(ach)
print(f"All distinct values: {all_ach}")

common = set_list
for ach in players.values():
    common = common.intersection(ach)
print(f"Common values: {common}\n")

for name, ach in players.items():
    others: set[str] = set()
    for name_other, ach_other in players.items():
        if name_other != name:
            others = others.union(ach_other)
    print(f"Only {name} has: {ach.difference(others)}\n")

for name, achievement in players.items():
    print(f"{name} is missing: {set_list.difference(achievement)}")
