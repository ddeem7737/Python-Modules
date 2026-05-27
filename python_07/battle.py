from ex0 import FlameFactory, AquaFactory
from ex0 import CreatureFactory

def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    