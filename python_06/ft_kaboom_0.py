from alchemy.grimoire import light_spell_record


if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimore module directly")

    print(
        "Testing record light spell: "
        f"{light_spell_record('Fantasy', 'Earth, wind and fire')}"
    )
