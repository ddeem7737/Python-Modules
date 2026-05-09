from typing import Generator
import random

players = ["Alex", "Bob", "John", "Osas", "Optimus", "Anakin",
           "George", "Misty", "Lea", "Sidius", "Robert", "Ilik"]

actions = ["walk", "kill", "breathe", "loot", "look", "execute",
           "love", "work", "help", "rule", "run", "sit", "eat"]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(events: list) -> Generator[tuple[str, str], None, None]:
    while events:
        index = random.randint(0, len(events) - 1)
        temp = events.pop(index)
        yield temp


print("=== Game Data Stream Processor ===")

gen = gen_event()

for i in range(1000):
    tup: tuple[str, str] = next(gen)
    print(f"Event {i}: Player {tup[0]} did action {tup[1]}")

events = []

for i in range(10):
    events.append(next(gen))

print(f"Built list of 10 events: {events}")

consume = consume_event(events)

for event in consume_event(events):
    print(f"Got event from list: {event}")
    print(f"Remains in list: {events}")
