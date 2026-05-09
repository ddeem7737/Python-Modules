import random

players = ["Alex", "Bob", "John", "osas", "Optimus", "Anakin",
           "George", "Misty", "Lea", "Sidius", "robert", "Ilik"]


print("=== Game Data Alchemist ===\n")

print(f"Initial list of players: {players}")

cap_list = [x.capitalize() for x in players]


print(f"New list with all names capitilized: {cap_list}")

is_cap_list = [x for x in players if x == x.capitalize()]

print(f"New list with all names capitalized: {is_cap_list}\n")
scores = {x: random.randint(0, 100) for x in cap_list}

print(f"Score dict: {scores}")

print(f"Score average: {round(sum(scores.values())/len(scores), 1)}")

high_scores = {x: y
               for x, y in scores.items()
               if y > sum(scores.values())/len(scores)}

print(f"High Scores: {high_scores}")
