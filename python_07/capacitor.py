from ex0.creature import CreatureFactory, Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def test_healing(factory: CreatureFactory) -> None:
    print("Testing Creature with healing capability")
    for label, creature in [("base", factory.create_base()),
                             ("evolved", factory.create_evolved())]:
        print(f" {label}:")
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, HealCapability):
            print(creature.heal())


def test_transform(factory: CreatureFactory) -> None:
    print("Testing Creature with transform capability")
    for label, creature in [("base", factory.create_base()),
                             ("evolved", factory.create_evolved())]:
        print(f" {label}:")
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())


if __name__ == "__main__":
    test_healing(HealingCreatureFactory())
    print()
    test_transform(TransformCreatureFactory())