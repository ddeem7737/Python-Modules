def validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = ["earth", "air", "fire", "water"]
    lower_ingredients: str = ingredients.lower()

    for ingredient in allowed:
        if ingredient in lower_ingredients:
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
