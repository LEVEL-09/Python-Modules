def validate_ingredients(ingredients: str) -> str:
    allowed = ("fire", "earth", "air", "water")
    if all(i in allowed for i in ingredients.split()):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
