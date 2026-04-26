def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    validate_result = validate_ingredients(ingredients)
    if validate_result == f"{ingredients} - VALID":
        return f"Spell recorded: {spell_name} ({validate_result})"
    return f"Spell rejected: {spell_name} ({validate_result})"
